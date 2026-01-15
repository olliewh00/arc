import psutil
import datetime

CPU_THRESHOLD = 80
MEMORY_THRESHOLD = 80

def check_system():
    cpu_usage = psutil.cpu_percent(interval=1)
    memory_usage = psutil.virtual_memory().percent
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    print(f"{timestamp} - CPU Usage: {cpu_usage}%")
    print(f"{timestamp} - Memory Usage: {memory_usage}%")

    if cpu_usage > CPU_THRESHOLD or memory_usage > MEMORY_THRESHOLD:
        print(f"ALERT: High system usage detected at {timestamp}")

if __name__ == "__main__":
    check_system()