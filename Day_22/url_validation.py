import requests

try:
    url = "http://api.ipapi.com/api/161.185.160.93?access_key=6cb199ac1233f86bd3c81759e3559fc5"
    response = requests.get(url)

    data = response.json()
    print("Status:",response.status_code)
    # Check if API returned an error
    if "error" in data:
        print("API Error:", data["error"]["info"])
    else:
        print("Successful")
        print(data)

except Exception as e:
    print("Error! Validation failed:", e)