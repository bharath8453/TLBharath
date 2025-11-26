import json

with open("sample2.json") as f:
    data = json.load(f)

#print(data)
#print(type(data))

print(data["shoppingList"]["groceries"])       # for nested case


