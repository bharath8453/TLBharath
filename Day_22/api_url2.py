import requests
import json
url = "https://api.open-meteo.com/v1/forecast?latitude=13.4005&longitude=78.0517&hourly=temperature_2m"
response = requests.get(url)
data = response.json()
print(data)

with open("file2.json", "w") as file:
    json.dump(data, file, indent=2)