# Прочитать сохраненный json-файл и записать данные на диск в csv-файл,
# первой строкой которого озаглавив каждый столбец и добавив новый столбец "телефон"
import json
import csv

names_rows = ["id", "name", "age", "phone"]

# считываем данные из json
with open("marina_hw7_3.json", "r") as file:
    data = json.load(file)
# записываем в csv
with open("marina_hw7_4.csv", "w", newline="") as file:
    wr = csv.DictWriter(file, names_rows)
    wr.writeheader()
    for key, value in data.items():
        wr.writerow({"id": key, "name": value[0], "age": value[1], "phone": ""})
