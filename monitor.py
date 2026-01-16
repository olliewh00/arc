import psutil
import datetime
import os
import time


import csv

FILE_NAME = "system_monitor.csv"
CPU_THRESHOLD = 80
MEMORY_THRESHOLD = 80

def check_system():
    cpu_usage = psutil.cpu_percent(interval=1)
    memory_usage = psutil.virtual_memory().percent
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    file_exist = os.path.isfile(FILE_NAME)

    with open (FILE_NAME, mode = 'a', newline='') as file:
        writer = csv.writer(file)
        if not file_exist:
            writer.writerow(["Timestamp", "CPU Usage", "Memory Usage"])
        writer.writerow([timestamp, cpu_usage, memory_usage])
    return f"{timestamp} - CPU Usage: {cpu_usage}%", f"{timestamp} - Memory Usage: {memory_usage}%"

if __name__ == "__main__":
   print("Monitoring has begun... Press Ctrl+C to stop.")
   try:
    while True:
        status = check_system()
        print(status)
        time.sleep(5)
   except KeyboardInterrupt:
        print("\n Monitoring has stopped.")