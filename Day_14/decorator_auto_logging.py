import requests
import logging

# Step 3: Logging Setup
logging.basicConfig(
    filename="decorator_log.txt",
    level=logging.INFO,
    format="%(asctime)s - %(message)s"
)

# Step 3: Decorator to auto-log function calls
def auto_log(func):
    def wrapper(*args, **kwargs):
        logging.info(f"Function '{func.__name__}' called with args={args} kwargs={kwargs}")
        return func(*args, **kwargs)
    return wrapper

# Step 2: API Function
@auto_log   # Step 4: Apply decorator
def fetch_api(url):
    response = requests.get(url, timeout=3)
    return response.status_code

# Another sample function
@auto_log
def add(a, b):
    return a + b

# Step 5: Testing
print(fetch_api("https://jsonplaceholder.typicode.com/todos/1"))
print(add(5, 10))