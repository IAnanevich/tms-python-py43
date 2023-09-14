# Создать список поездов. Структура словаря: номер поезда,
# пункт и время прибытия, пункт и время отбытия.
# Вывести все сведения о поездах, время пребывания в пути
# которых превышает 7 часов 20 минут.

# from datetime import datetime, timedelta
#
# list_of_trains = [
#     {"number": "1", "point A": "station 1", "start": datetime(2023, 8, 10, 22, 30), "point B": "Station 2", "end": datetime(2023, 8, 11, 00, 24)},
#     {"number": "2", "point A": "station 3", "start": datetime(2023, 9, 23, 9, 36), "point B": "Station 4", "end": datetime(2023, 9, 24, 23, 17)},
#     {"number": "3", "point A": "station 5", "start": datetime(2023, 2, 10, 10, 5), "point B": "Station 6", "end": datetime(2023, 2, 11, 22, 10)},
#     {"number": "4", "point A": "station 7", "start": datetime(2023, 8, 27, 4, 30), "point B": "Station 8", "end": datetime(2023, 8, 27, 5, 24)},
#     {"number": "5", "point A": "station 9", "start": datetime(2023, 8, 10, 17, 17), "point B": "Station 10", "end": datetime(2023, 8, 12, 0, 9)}
# ]
#
# def time_def(list_our):
#     for i in list_our:
#         print(i['end'] - i['start'] > timedelta(hours=7, minutes=20))
#         return i['end'] - i['start']
#
# print(time_def(list_of_trains))

# for i in list_of_trains:
#     if time_def(list_of_trains) >= timedelta(hours=7, minutes=20):
#         print(f'Поезд № {i["number"]}')
