# Прочитать сохраненный json-файл и записать данные на диск в csv-файл, первой
# строкой которого озаглавив каждый столбец и добавив новый столбец "телефон".
import json
import csv


if __name__ == "__main__":
    with open('clients.json') as json_file, \
            open('clients.csv', 'w', newline='') as csv_file:
        csv_writer = csv.DictWriter(csv_file, fieldnames=['id', 'name', 'age', 'phone'])
        csv_writer.writeheader()
        clients = json.load(json_file)
        for key, value in clients.items():
            csv_writer.writerow({
                'id': key,
                'name': value[0],
                'age': value[-1],
                'phone': '097-32-88'
            })
