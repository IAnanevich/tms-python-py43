# Прочитать сохраненный json-файл. Записать данные на диск
# в csv-файл добавив новый стоблец "телефон

import csv
import json

with open("katya_7_3.json", "r") as new_file_json:
    file_katya = json.loads(new_file_json.read())
    with open("katya_7_4.csv", "w") as new_file_csw:
        writer = csv.DictWriter(new_file_csw, fieldnames=["id", "name", "years", "phone"])
        writer.writeheader()
        for key, value in file_katya.items():
            writer.writerow({"id": key, "name": value[0], "years": value[1], "phone": "+375 29"})
