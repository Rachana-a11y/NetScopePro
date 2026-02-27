# COMMON_PORTS = {
#     21: "FTP",
#     22: "SSH",
#     23: "TELNET",
#     25: "SMTP",
#     53: "DNS",
#     80: "HTTP",
#     110: "POP3",
#     139: "NetBIOS",
#     143: "IMAP",
#     443: "HTTPS",
#     445: "SMB",
#     3306: "MySQL",
#     3389: "RDP",
#     8080: "HTTP-ALT"
# }

# def detect_service(port):
#     return COMMON_PORTS.get(port, "Unknown")

# Extended Service Port Database

COMMON_PORTS = {

    # File Transfer
    20: "FTP-Data",
    21: "FTP",
    989: "FTPS-Data",
    990: "FTPS",

    # Remote Access
    22: "SSH",
    23: "TELNET",
    3389: "RDP",
    5900: "VNC",

    # Email
    25: "SMTP",
    465: "SMTPS",
    587: "SMTP-Submission",
    110: "POP3",
    995: "POP3S",
    143: "IMAP",
    993: "IMAPS",

    # Web
    80: "HTTP",
    443: "HTTPS",
    8080: "HTTP-ALT",
    8443: "HTTPS-ALT",
    8000: "HTTP-Dev",
    8888: "HTTP-Proxy",

    # DNS
    53: "DNS",

    # Database
    1433: "MSSQL",
    1521: "Oracle DB",
    3306: "MySQL",
    5432: "PostgreSQL",
    27017: "MongoDB",
    6379: "Redis",

    # Windows Services
    135: "MSRPC",
    139: "NetBIOS",
    445: "SMB",

    # Network Services
    67: "DHCP",
    68: "DHCP-Client",
    123: "NTP",
    161: "SNMP",
    389: "LDAP",
    636: "LDAPS",

    # DevOps / Containers
    2375: "Docker",
    2376: "Docker-SSL",
    6443: "Kubernetes API",

    # Monitoring
    9200: "Elasticsearch",
    5601: "Kibana",

    # Misc
    69: "TFTP",
    514: "Syslog",
    179: "BGP"
}

def detect_service(port):
    return COMMON_PORTS.get(port, "Unknown Service")