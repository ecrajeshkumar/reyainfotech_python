
import csv

# Writing data to CSV
with open("data.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Name", "Age", "City"])   # header
    writer.writerow(["Rajesh", 35, "Pune"])
    writer.writerow(["Punam", 32, "Pune"])

with open("data.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

import json

data = {
    "name": "Rajesh",
    "age": 35,
    "skills": ["Python", "AI", "C++"]
}

with open("data.json", "w") as file:
    json.dump(data, file, indent=4)

with open("data.json", "r") as file:
    data = json.load(file)
    print("Name ", data["name"])   # Output: Rajesh
    print("age ", data["age"])    # Output: 35
    print("skills ", data["skills"]) # Output: ['Python', 'AI', 'C++']

