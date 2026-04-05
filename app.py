"""
Jenkins Remoting Demo App — CodeAlpha DevOps Internship Task 2
This script is distributed and executed across remote Jenkins agents.
"""

import platform
import socket
import os
from datetime import datetime

def get_system_info():
    return {
        "hostname":    socket.gethostname(),
        "os":          platform.system(),
        "os_version":  platform.version(),
        "architecture": platform.machine(),
        "python":      platform.python_version(),
        "node_name":   os.getenv("NODE_NAME", "local"),
        "build_number": os.getenv("BUILD_NUMBER", "N/A"),
        "timestamp":   datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    }

def run():
    print("=" * 55)
    print("   Jenkins Remoting Demo — CodeAlpha DevOps Task 2")
    print("=" * 55)

    info = get_system_info()
    for key, value in info.items():
        print(f"  {key:<18}: {value}")

    print("=" * 55)
    print("  ✅ App executed successfully on remote Jenkins agent")
    print("=" * 55)

if __name__ == "__main__":
    run()
