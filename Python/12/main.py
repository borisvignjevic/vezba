
import json

with open("data.json", 'r') as file:
    data = json.load(file)
    data.append({
        "name": "Vuk Vignjevic",
        "age": 12,
        "height": 150,
        "gander": "male"
    })

print(data)

with open("data.json", 'w')as file:
    json.dump(data, file, indent=4)