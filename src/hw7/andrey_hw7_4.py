# Прочитать сохранённый json-файл и записать данные на диск в csv-файл,
# первой строкой которого озаглавив каждый столбец и добавив новый столбец 'телефон'.

import json
import csv

if __name__ == "__main__":
    with open('example.json', 'r') as file_json:
        try:
            var = json.load(file_json)
        except ValueError as e:
            print(e)
        else:
            with open('example.csv', 'w', newline='') as file_csv:
                fieldnames = ['ID', 'Name', 'Age', 'Phone']
                writer = csv.DictWriter(file_csv, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows([dict(ID=key, Name=value[0], Age=value[1], Phone='+3') for key, value in var.items()])
