import requests
import json
url = "https://api.open-meteo.com/v1/forecast?latitude=17.6801&longitude=83.2016&hourly=temperature_2m"
response = requests.get(url)
data = response.json()
print(data)

with open("file.json", "w") as file:
    json.dump(data, file, indent=2)
