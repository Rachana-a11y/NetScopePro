import argparse
from scanner import scan_target
from risk_engine import analyze_risk
from report import generate_report

def main():
    parser = argparse.ArgumentParser(description="NetScope Pro")
    parser.add_argument("target")
    parser.add_argument("--full", action="store_true")
    args = parser.parse_args()

    ports = range(1, 65536) if args.full else range(1, 1025)

    results, os_guess, scan_time = scan_target(args.target, ports)
    score, level, recommendations = analyze_risk(results)

    print("\n===== NETSCOPE PRO REPORT =====")
    print("Target:", args.target)
    print("Open Ports:", len(results))
    print("OS Guess:", os_guess)
    print("Risk Level:", level)
    print("Scan Time:", scan_time, "seconds")

    generate_report(args.target, results, level, recommendations, scan_time)

if __name__ == "__main__":
    main()