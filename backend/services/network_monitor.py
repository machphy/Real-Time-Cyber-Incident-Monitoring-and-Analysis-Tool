import psutil
import socket
import time
import json

def get_network_connections():
    connections = psutil.net_connections(kind='inet')
    suspicious_ports = [4444, 6667, 1337]  # Example of suspicious ports
    detected_threats = []

    for conn in connections:
        if conn.status == 'ESTABLISHED' and conn.laddr.port in suspicious_ports:
            detected_threats.append({
                "type": "Suspicious Network Connection",
                "severity": "High",
                "source_ip": conn.laddr.ip,
                "destination_ip": conn.raddr.ip if conn.raddr else "Unknown",
                "timestamp": time.strftime('%Y-%m-%d %H:%M:%S')
            })
    
    return detected_threats

if __name__ == "__main__":
    while True:
        threats = get_network_connections()
        if threats:
            print(json.dumps(threats, indent=4))
        time.sleep(5)

import logging
logging.basicConfig(filename="backend/logs/network_monitor.log", level=logging.INFO)
logging.info("🚀 Network Monitor Started")
