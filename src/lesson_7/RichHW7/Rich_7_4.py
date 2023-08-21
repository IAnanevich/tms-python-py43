# 1. Прочитать сохраненный json-файл. Записать данные на диск в csv-файл первой строкой,
# которого озоглавив каждый столбец и добавив новый стоблец телефон


import csv

with open('people.json', 'r') as name_json:
    with open('people.csv', 'w') as name_csv:
        writer = csv.writer(name_csv)
        writer.writerow(['id', 'name', 'years', 'phone'])
        for i in name_json:
            name_csv.write(i)
