import time

def monitor():
    print("[+] eBPF IDS started")
    
    events = [
        "execve detected",
        "file access /etc/shadow",
        "network connection suspicious",
        "privilege escalation attempt"
    ]

    for event in events:
        print(f"[ALERT] {event}")
        time.sleep(1)

if __name__ == "__main__":
    monitor()