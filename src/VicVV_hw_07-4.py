# Запись в файл csv из json

import json
import csv

with open("example.json", "r") as json_file:
    _dict = json.load(json_file)
# print(_dict)
_line = ['id', 'name', 'age', 'phone']
with open('example.csv', 'w', newline='') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(_line)
    for k, v in _dict.items():
        # print(k)
        # print(v)
        _line[0] = k
        _line[1] = v[0]
        _line[2] = v[1]
        _line[3] = None
        writer.writerow(_line)
