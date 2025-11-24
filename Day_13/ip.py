import subprocess
import os

ip_list = ["127.0.0.1", "8.8.8.8", "192.168.1.99"]

for ip in ip_list:
    # Determine the correct ping command based on the operating system
    if os.name == 'nt': # For Windows
        command = ['ping', '-n', '1', ip]
    else: # For Linux/macOS
        command = ['ping', '-c', '1', ip]
    
    # Execute the ping command
    result = subprocess.run(command, capture_output=True, text=True)

    # Check the return code
    if result.returncode == 0:
        print(f"IP address {ip} is reachable.")
    else:
        print(f"IP address {ip} is unreachable.")