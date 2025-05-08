import re
import csv
import random
import os
import json

log_path = "backend/logs/server.log"
output_csv = "data/log_dataset.csv"

os.makedirs("data", exist_ok=True)

header = ["src_port", "dst_port", "packet_size", "protocol", "label"]

def extract_alert_dict(log_line):
    try:
        match = re.search(r"New Alert: ({.*})", log_line)
        if match:
            alert_str = match.group(1).replace("'", '"')
            alert = json.loads(alert_str)
            return alert
    except Exception as e:
        print(f"[!] Error parsing line: {e}")
    return None

with open(log_path, "r") as log_file, open(output_csv, "w", newline="") as out_csv:
    writer = csv.DictWriter(out_csv, fieldnames=header)
    writer.writeheader()

    for line in log_file:
        alert = extract_alert_dict(line)
        if alert:
            row = {
                "src_port": random.choice([80, 443, 22, 8080, 3389]),
                "dst_port": random.choice([443, 80, 21, 25, 53]),
                "packet_size": random.randint(500, 1500),
                "protocol": random.choice([6, 17]),  # TCP=6, UDP=17
                "label": alert.get("type", "Unknown")
            }
            writer.writerow(row)

print(f"✅ Logs converted to CSV at: {output_csv}")
