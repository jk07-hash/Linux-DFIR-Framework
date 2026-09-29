import platform
import socket
import getpass
from datetime import datetime


def collect_system_info():
    info = {
        "hostname": socket.gethostname(),
        "username": getpass.getuser(),
        "os": platform.system(),
        "os_version": platform.version(),
        "architecture": platform.machine(),
        "processor": platform.processor(),
        "collection_time": datetime.now().isoformat()
    }

    return info


if __name__ == "__main__":
    data = collect_system_info()

    print("\n=== Linux Forensic System Information ===")

    for key, value in data.items():
        print(f"{key}: {value}")
