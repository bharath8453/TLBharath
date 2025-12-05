import json
import requests
# import time 
t = 1
while(t <= 102):
    url =requests.get('https://api.nationalize.io/?name=bharath')
    data = url.json()
    data1 = url.status_code
    t = t+2
    print(t)
    print(data)
    print(data1)