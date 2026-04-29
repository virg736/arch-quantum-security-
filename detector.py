import time
import subprocess

def get_logs():
    try:
        logs = subprocess.check_output(
            ["journalctl", "-n", "10", "--no-pager"],
            text=True
        )
        return logs.split("\n")
    except:
        return ["no logs"]

def analyze(logs):
    alerts = []

    for line in logs:
        if "failed" in line.lower():
            alerts.append("Brute force attempt")

        if "sudo" in line.lower():
            alerts.append("Privilege escalation")

    return alerts

if __name__ == "__main__":
    logs = get_logs()
    alerts = analyze(logs)

    for alert in alerts:
        print(f"[ALERT] {alert}")

    print("[+] Scan complete")