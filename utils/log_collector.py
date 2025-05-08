import os
import requests
import pandas as pd
import time
from datetime import datetime

# Ensure the directory exists
DATASET_PATH = "data_pipeline/log_dataset.csv"
os.makedirs("data_pipeline", exist_ok=True)

def parse_log_line(log_line):
    """
    Dummy parser: Customize this based on your log format.
    Example: "2024-04-10 12:34:56 - INFO - 🔔 New Alert: {'type': 'DDoS', 'severity': 'High', 'source_ip': '192.168.1.10', ...}"
    """
    try:
        if "New Alert:" in log_line:
            log_data = log_line.split("New Alert:")[1].strip()
            log_dict = eval(log_data)  # ⚠️ Safer alternative: use json.loads if logs are JSON
            return {
                "timestamp": log_dict.get("timestamp"),
                "src_ip": log_dict.get("source_ip"),
                "type": log_dict.get("type"),
                "severity": log_dict.get("severity"),
                "label": log_dict.get("type")  # Use type as temporary label
            }
    except Exception as e:
        print("Parsing error:", e)
    return None

def fetch_and_save_logs():
    all_data = []

    print("📥 Collecting logs from API...")
    for _ in range(10):  # Adjust loop count as needed
        try:
            res = requests.get("http://127.0.0.1:5000/api/logs")
            if res.status_code == 200:
                logs = res.json().get("logs", [])
                for log in logs:
                    parsed = parse_log_line(log)
                    if parsed:
                        all_data.append(parsed)
        except Exception as e:
            print(f"❌ Error fetching logs: {e}")
        time.sleep(2)

    # Save to CSV
    if all_data:
        df = pd.DataFrame(all_data)
        if os.path.exists(DATASET_PATH):
            df.to_csv(DATASET_PATH, mode='a', header=False, index=False)
        else:
            df.to_csv(DATASET_PATH, index=False)
        print(f"✅ Logs saved to {DATASET_PATH}")
    else:
        print("⚠️ No data parsed.")

if __name__ == "__main__":
    fetch_and_save_logs()
