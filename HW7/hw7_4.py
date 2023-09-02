# 1. Прочитать сохраненный json-файл
# 2. Записать данные на диск в csv-файл
#       первой строкой, которого?
#       озоглавив каждый столбец и добавив новый стоблец "телефон"
import json
import csv

# some_data = None
json_file = "hw7_3.json"
csv_file = "hw7_4.csv"

# 1. Прочитать сохраненный json-файл
with open(json_file, "r") as some_file:
    some_data = json.loads(some_file.read())

# Проверка
print(type(some_data))
print(some_data)

# 2. Подготовка данyых:  озоглавив каждый столбец и добавив новый стоблец "телефон"
prepared_data = list()
for some_item in some_data.items():
    prepared_data.append({"id": some_item[0], "name": some_item[1][0], "age": some_item[1][1], "telephone": "+375 29 "})

# 2. Записать данные на диск в csv-файл
with open(csv_file, 'w') as some_file:
    csv_writer = csv.DictWriter(some_file, fieldnames=prepared_data[0].keys())
    csv_writer.writeheader()
    for line in prepared_data:
        csv_writer.writerow(line)
