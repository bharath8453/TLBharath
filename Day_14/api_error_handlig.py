import requests
import json

def fetch_api_data(url):
    """
    Fetch data from an API with strong error handling.
    Handles:
    - timeout
    - host unreachable
    - invalid URLs
    - non-JSON responses
    - HTTP error status codes
    """
    try:
        # Make HTTP GET request with 3 second timeout
        response = requests.get(url, timeout=3)

        # Raise error if status code is 4xx or 5xx
        response.raise_for_status()

        # Try to parse JSON response
        try:
            data = response.json()
            return data

        except json.JSONDecodeError:
            print(f"❌ NON-JSON response received from: {url}")
            return None

    except requests.exceptions.Timeout:
        print(f"❌ Timeout occurred while accessing: {url}")
        return None

    except requests.exceptions.ConnectionError:
        print(f"❌ Host unreachable: {url}")
        return None

    except requests.exceptions.InvalidURL:
        print(f"❌ Invalid URL format: {url}")
        return None

    except requests.exceptions.HTTPError as e:
        print(f"❌ HTTP error: {e} for URL: {url}")
        return None

    except Exception as e:
        print(f"❌ Unexpected error for URL {url}: {e}")
        return None

#print("\n=== TESTING GOOD URL ===")
#good = fetch_api_data("https://jsonplaceholder.typicode.com/todos/1")
#print("Result:", good)

#print("\n=== TESTING HOST UNREACHABLE ===")
#fetch_api_data("https://no-such-domain-9999999.com/data")

print("\n=== TESTING INVALID URL ===")
fetch_api_data("ht!tp://bad#url")

print("\n=== TESTING NON-JSON RESPONSE ===")
fetch_api_data("https://www.google.com")

print("\n=== TESTING 404 NOT FOUND ===")
fetch_api_data("https://jsonplaceholder.typicode.com/invalid-endpoint")
