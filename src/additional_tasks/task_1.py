# Создать список поездов. Структура словаря: номер поезда,
# пункт и время прибытия, пункт и время отбытия.
# Вывести все сведения о поездах, время пребывания в пути
# которых превышает 7 часов 20 минут.

from datetime import datetime

# datetime.time(hour, minute)

# list_of_trains = [
#     {"number": "1", "point A": "", "start": datetime.time(5, 14), "point B": "", "end": datetime.time(18, 35)},
#     {"number": "2", "point A": "", "start": datetime.time(00, 43), "point B": "", "end": datetime.time(20, 35)},
#     {"number": "3", "point A": "", "start": datetime.time(18, 22), "point B": "", "end": datetime.time(21, 35)},
# ]
#
#
# print(list_of_trains[1])
# for i in list_of_trains:
#     if i["end"] - i["start"] == 0:
#         print(i["end"] - i["start"])
