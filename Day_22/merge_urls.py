import requests
import json
url1 = "https://marine-api.open-meteo.com/v1/marine?latitude=13.3347&longitude=74.7462&hourly=wave_height"
response1 = requests.get(url1)

url2 = "https://api.open-meteo.com/v1/forecast?latitude=13.4005&longitude=78.0517&hourly=temperature_2m"
response2 = requests.get(url2)

final_output = {
    "location_1": {
        "status": response1.status_code,
        "data": response1.json()
    },
    "location_2": {
        "status": response2.status_code,
        "data": response2.json()
    }
}
with open("file3.json","w") as file:
    file.write(json.dumps(final_output, indent=4))