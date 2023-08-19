# Прочитать сохраненный json-файл. Записать данные на диск
# в csv-файл добавив новый стоблец "телефон

import csv
import json

with open('katya_7_3.json', 'r') as new_file_json:
    file_katya = json.loads(new_file_json.read())
    with open('katya_7_4.csv', 'w') as new_file_csw:
        writer = csv.writer(new_file_csw, delimiter=';')
        writer.writerow(['id', 'name', 'years', 'phone', file_katya])
        for line in new_file_json:
            new_file_csw.write(line)
