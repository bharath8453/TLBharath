import json

with open("wireshark_wifi.json") as f:
    data = json.load(f)

for user in data:
    print(data[0]["_index"])