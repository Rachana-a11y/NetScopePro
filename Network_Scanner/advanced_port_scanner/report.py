# def generate_report(target, results, level, recommendations, scan_time):
#     with open("netscope_report.txt", "w") as f:
#         f.write("NETSCOPE PRO – SECURITY ASSESSMENT REPORT\n")
#         f.write("=========================================\n\n")
#         f.write(f"Target: {target}\n")
#         f.write(f"Total Open Ports: {len(results)}\n")
#         f.write(f"Risk Level: {level}\n")
#         f.write(f"Scan Duration: {scan_time} seconds\n\n")

#         f.write("Open Ports & Services:\n")
#         f.write("----------------------\n")

#         for r in results:
#             f.write(f"{r['port']} | {r['service']} | {r['banner']}\n")

#         if recommendations:
#             f.write("\nSecurity Recommendations:\n")
#             for rec in recommendations:
#                 f.write(f"- {rec}\n")


import os

def generate_report(target, results, level, recommendations, scan_time):
    if not os.path.exists("output"):
        os.makedirs("output")

    report_file = os.path.join("output", "netscope_report.txt")

    with open(report_file, "w") as f:
        f.write("NETSCOPE PRO – SECURITY ASSESSMENT REPORT\n")
        f.write("=========================================\n\n")
        f.write(f"Target: {target}\n")
        f.write(f"Total Open Ports: {len(results)}\n")
        f.write(f"Risk Level: {level}\n")
        f.write(f"Scan Duration: {scan_time} seconds\n\n")

        f.write("Open Ports & Services:\n")
        f.write("----------------------\n")

        for r in results:
            f.write(f"{r['port']} | {r['service']} | {r['banner']}\n")

        if recommendations:
            f.write("\nSecurity Recommendations:\n")
            for rec in recommendations:
                f.write(f"- {rec}\n")

    print(f"\n[+] Report saved to: {report_file}")