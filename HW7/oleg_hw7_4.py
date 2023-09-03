"""
из pdf текст копируется криво. но суть ясна думаю
. - - , Прочитать с файломох преобразований выводить на экран).ранённый json('example.txt','r') файл и з example.txtапис файломать данные на дис файломк в csv-файл, первой файл первой
с файломтрокой которого оз example.txtаглавив каждый с файломтолбец и добавив новый столбец “телефон”. и добавив новый с файломтолбец и добавив новый столбец “телефон”. “телефон”. .
"""
import json
import csv


items = [["ID", "NAME", "AGE", "PHONE"]]
try:
    # получаем json и формируем массив items
    with open("class_at_school_2.json") as f:
        for key, value in json.load(f).items():
            items.append([key, value[0], value[1], "+375(XX)XXX-XX-XX"])
except EnvironmentError as error:
    print("Ошибка при чтении файла " + error)
else:
    try:
        # пишим массив в новый файл
        with open("class_at_school_2.csv", "w", newline="") as csv_file:
            writer = csv.writer(csv_file, delimiter=";")
            writer.writerows(items)
    except EnvironmentError as error:
        print("Ошибка при записи в файл " + error)

# получилось как то громоздко, но может и пойдет) второй try может не стоило в else пихать, а отдельно...
