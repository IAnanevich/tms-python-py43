import csv
import json

with open('lines.json', 'r') as file_j:
    data = json.load(file_j)
    with open('lines.csv', 'w') as file_c:
        writer = csv.writer(file_c)
        writer.writerow(
            (
                'id',
                'name',
                'age',
                'phone''\n',
                data
            )

        )
