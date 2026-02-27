def analyze_risk(results):
    score = 0
    recommendations = []

    risky_ports = {
        21: "Disable FTP. Use SFTP instead.",
        23: "Telnet is insecure. Replace with SSH.",
        445: "Restrict SMB via firewall.",
        3389: "Restrict RDP access using VPN.",
        3306: "Database exposed. Restrict external access."
    }

    score += len(results)

    for r in results:
        if r["port"] in risky_ports:
            score += 5
            recommendations.append(risky_ports[r["port"]])

    if score > 20:
        level = "HIGH"
    elif score > 10:
        level = "MEDIUM"
    else:
        level = "LOW"

    return score, level, recommendations