import os
import time

WATCH_DIRECTORY = "/media/"  # Change based on your system (Linux: /media/, Windows: E:/)

def monitor_usb():
    known_devices = set(os.listdir(WATCH_DIRECTORY))

    while True:
        current_devices = set(os.listdir(WATCH_DIRECTORY))
        new_devices = current_devices - known_devices

        for device in new_devices:
            print(f"🚨 Alert: New USB device detected: {device}")

        known_devices = current_devices
        time.sleep(5)

if __name__ == "__main__":
    monitor_usb()
