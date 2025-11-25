import requests

# Custom Exception
class APIResponseError(Exception):
    pass

def fetch_api_data(url):
    try:
        print(f"\nFetching: {url}")
        r = requests.get(url, timeout=3)

        if not r.ok:
            raise APIResponseError(f"HTTP Error {r.status_code}")

        try:
            return r.json()
        except:
            raise APIResponseError("Non-JSON response")

    except requests.exceptions.Timeout:
        raise APIResponseError("Timeout error")

    except requests.exceptions.ConnectionError:
        raise APIResponseError("Host unreachable")

    except Exception as e:
        raise APIResponseError(f"Unexpected: {e}")


# Test function
def test(url):
    try:
        print("Result:", fetch_api_data(url))
    except APIResponseError as e:
        print("❌", e)


# Test URLs
good = "https://jsonplaceholder.typicode.com/todos/1"
bad = "https://invalid-domain.com"
non_json = "https://www.google.com"
server_error = "https://httpbin.org/status/500"

test(good)
test(bad)
test(non_json)
test(server_error)