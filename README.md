# Project 01: Containerized System Monitor 🖥️ 🐳

A professional Python-based utility that monitors system resources (CPU/RAM), logs telemetry data to a persistent CSV database, and operates within a fully isolated Docker environment.

## 🚀 The Mission
This project demonstrates the transition from a local script to a **Production-Ready** tool. It solves the "It works on my machine" problem by using Docker to ensure environment parity across macOS, Windows, and Linux.

### Key Features:
- **Telemetry Engine:** Real-time tracking of CPU and Memory usage via `psutil`.
- **Persistent Data:** Automatic CSV logging with header detection and row-appending logic.
- **Dockerized Architecture:** Built with a `python:3.9-slim` base image for a minimal security footprint.
- **Mac-Optimized:** Configured with `PYTHONUNBUFFERED` environment variables to ensure real-time log streaming in Docker Desktop.

---

## 🛠️ Tech Stack
- **Language:** Python 3.9
- **Core Libraries:** `psutil`, `csv`, `datetime`
- **DevOps:** Docker (Containerization)

---

## 📦 Installation & Execution

### 1. Build the Image
```bash
docker build -t resource-monitor .