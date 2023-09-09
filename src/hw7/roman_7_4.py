'''Прочитать сохраненный json-файл. Записать данные на диск в csv-файл первой строкой,
которого озоглавив каждый столбец и добавив новый стоблец телефон'''
import json
import csv

file_name = "data.json"

# Чтение данных из JSON-файла
with open(file_name) as json_file:
    data = json.load(json_file)

# Создание списка данных для записи в CSV-файл
data_list = [["ID", "Name", "Age", "Phone"]]

for id_number, (name, age) in data.items():
    phone = "+375"
    data_list.append([id_number, name, age, phone])

# Запись данных в CSV-файл
csv_file_name = "data.csv"
with open(csv_file_name, mode='w', newline='') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerows(data_list)

print(f'Данные записаны в CSV-файл: {csv_file_name}')
