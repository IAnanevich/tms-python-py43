"""4. Прочитать сохранённый json-файл и записать данные на диск в csv-файл,
первой строкой которого озаглавив каждый столбец и добавив новый столбец "телефон"."""
import csv

with open('nastya_hw7_3.json', 'r') as f_json:
    with open('nastya_hw7_4.csv', 'w') as f_csv:
        writer = csv.writer(f_csv)
        writer.writerow(['id', 'name', 'years', 'phone'])
        for i in f_json:
            f_csv.write(i)
