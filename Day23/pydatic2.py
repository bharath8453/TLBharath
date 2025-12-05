import json

with open("file.json", "r") as file:
    data_dict = json.load(file)

print(data_dict)
print(type(data_dict))
