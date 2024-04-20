import json
import csv

with open('problems.json', 'r') as json_file:
    data = json.load(json_file)

with open('problems.csv', 'w', newline='') as csv_file:
    writer = csv.DictWriter(csv_file, fieldnames = list(data[0].keys()))
    writer.writeheader()
    for item in data:
        writer.writerow(item)