import logging
logging.basicConfig(filename='log.txt',level=logging.WARNING)
logging.debug("This is debug")
logging.info("Program started")
logging.warning("warning Information")
logging.error("error Information")
logging.critical("Critical Information")
import subprocess


ip_list = [
    "192.168.1.1",
    "8.8.8.8",
    "10.0.0.1",
    "192.168.56.1"
]

for ip in ip_list:
    print(f"Checking {ip} ...")

    try:
        # ping with 1 packet, -w 500 means 500ms timeout in Windows
        command = ["ping", "-n", "1", "-w", "500", ip]

        result = subprocess.run(
            command,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            timeout=1  # safeguard timeout
        )

        if result.returncode == 0:
            # Even though ping succeeded, check if time > 500ms
            output = result.stdout.decode(errors="ignore")

            # Extract "time" value from ping output
            if "time=" in output:
                # Example: time=23ms
                part = output.split("time=")[1]
                ms = part.split("ms")[0]

                # Remove any unwanted chars
                try:
                    ms_value = int(''.join(filter(str.isdigit, ms)))
                except:
                    ms_value = 0

                if ms_value > 10:
                    print(f"IP address {ip} reachable but SLOW PING ({ms_value} ms)\n")
                else:
                    print(f"IP address {ip} is reachable ({ms_value} ms).\n")
            else:
                print(f"IP address {ip} is reachable.\n")

        else:
            print(f"IP address {ip} is unreachable.\n")

    except subprocess.TimeoutExpired:
        print(f"IP address {ip} is reachable but SLOW PING (timeout > 10ms)\n")

    except Exception as e:
        print(f"Error pinging {ip}: {e}\n")