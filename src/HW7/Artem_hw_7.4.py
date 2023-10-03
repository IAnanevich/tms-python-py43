# Прочитать сохраненный json-файл и записать данные на диск в csv-файл,
# первой строкой которого озаглавив каждый столбец и добавив новый столбец "телефон"
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
