import subprocess

# ---------------- Task 1: IP Reachability Function ----------------
def check_ip_reachability():
    ip_list = [
        "192.168.1.1",
        "8.8.8.8",
        "10.0.0.1",
        "192.168.56.1"
    ]

    for ip in ip_list:
        print(f"\nChecking {ip} ...")
        command = ["ping", "-n", "1", ip]   # Use -c for Linux
        result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        if result.returncode == 0:
            print(f"IP address {ip} is reachable.")
        else:
            print(f"IP address {ip} is unreachable.")


# ---------------- Task 2: Latency Summary Functions ----------------
def calculate_average(data):
    return sum(data) / len(data)

def get_summary(data):
    return {
        "Min": min(data),
        "Max": max(data),
        "Average": calculate_average(data)
    }


# ---------------- Task 3: CLI Menu ----------------
while True:
    print("\n===== Network Utility Menu =====")
    print("1. Test IP Reachability")
    print("2. Latency Summary Calculator")
    print("3. Exit")
    
    choice = input("Enter your choice (1/2/3): ")

    # Choice 1: Call IP Reachability function
    if choice == "1":
        check_ip_reachability()

    # Choice 2: Latency Summary
    elif choice == "2":
        values = input("Enter comma-separated latency values: ")
        values_list = [float(x.strip()) for x in values.split(",")]

        summary = get_summary(values_list)
        print("\nLatency Summary:")
        print(summary)

    # Choice 3: Exit
    elif choice == "3":
        print("Exiting program...")
        break

    # Invalid input
    else:
        print("Invalid choice! Please enter 1, 2, or 3.")