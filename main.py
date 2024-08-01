print("God_Bless")

import json

with open("data.json") as file:
    data = json.load(file)
    data.append({
            "name": "Any",
            "age": "30",
            "height": 159,
            "gender": "female"
    })

print(data)

with open("data.json", "w") as file:
    json.dump(data, file, indent=4)