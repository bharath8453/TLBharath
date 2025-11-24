latency_data = [12.5, 15.2, 11.8, 14.1, 13.5, 16.0, 10.9, 14.8]

def calculate_average(data):
    if not data:
        return 0
    return sum(data) / len(data)

def get_summary(data):
    if not data:
        return {"Min": None, "Max": None, "Average": None}
    minimum_val = min(data)
    maximum_val = max(data)
    average_val = calculate_average(data)
    return {"Min": minimum_val, "Max": maximum_val, "Average": average_val}

summary_results = get_summary(latency_data)
print(f"Latency Summary: {summary_results}")
