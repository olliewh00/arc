# Project 01: Automated System Resource Monitor 🖥️

A professional-grade Python utility designed to monitor system vitals (CPU and RAM), log them into a persistent CSV database, and run within a Dockerized environment.

## 🚀 Overview
This project serves as the first entry in my **20-Projects-Challenge-2026**. It demonstrates the transition from a local Python script to a portable, containerized DevOps tool.

### Key Features:
- **Continuous Monitoring:** Real-time tracking of CPU and Memory usage.
- **Data Persistence:** Automatically logs data to a structured `system_monitor.csv`.
- **Environment Agnostic:** Fully Dockerized to ensure it runs on any machine without "dependency hell."
- **Robustness:** Handles graceful shutdowns (Ctrl+C) and unbuffered real-time logging.

---

## 🛠️ Tech Stack
- **Language:** Python 3.9+
- **Libraries:** `psutil` (System Monitoring), `csv`, `os`, `time`
- **DevOps:** Docker (Containerization)

---

## 📦 Installation & Setup

### 1. Local Setup
If you want to run it directly on your machine:
```bash
# Clone the repository
git clone [https://github.com/](https://github.com/)[YOUR_USERNAME]/Project-01-Resource-Monitor.git
cd Project-01-Resource-Monitor

# Create and activate virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the monitor
python monitor.py