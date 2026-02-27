import socket
import time
from concurrent.futures import ThreadPoolExecutor
from service_map import detect_service
from logger import log

def grab_banner(ip, port, domain):
    try:
        s = socket.socket()
        s.settimeout(1)
        s.connect((ip, port))

        if port in [80, 8080]:
            request = f"HEAD / HTTP/1.1\r\nHost: {domain}\r\nUser-Agent: Mozilla/5.0\r\n\r\n"
            s.send(request.encode())
        else:
            s.send(b"\r\n")

        banner = s.recv(1024).decode(errors="ignore").strip()
        s.close()
        return banner if banner else "No banner"
    except:
        return "No banner"

def scan_port(ip, port, domain):
    try:
        s = socket.socket()
        s.settimeout(0.5)
        result = s.connect_ex((ip, port))
        s.close()

        if result == 0:
            banner = grab_banner(ip, port, domain)
            service = detect_service(port)
            log(f"Open Port Found: {port}")
            return {
                "port": port,
                "service": service,
                "banner": banner
            }
    except:
        pass
    return None

def scan_target(target, ports):
    start_time = time.time()
    ip = socket.gethostbyname(target)
    open_ports = []

    print("\n[ Ethical Notice ]")
    print("Use this tool only on authorized systems.\n")

    with ThreadPoolExecutor(max_workers=300) as executor:
        results = list(executor.map(lambda p: scan_port(ip, p, target), ports))

    for r in results:
        if r:
            open_ports.append(r)

    os_guess = "Unknown"
    for r in open_ports:
        if r["port"] in [135, 445]:
            os_guess = "Windows Likely"
        elif r["port"] == 22:
            os_guess = "Linux/Unix Likely"
        elif r["port"] in [80, 443]:
            os_guess = "Web Server (Linux Likely)"

    scan_time = round(time.time() - start_time, 2)

    return open_ports, os_guess, scan_time