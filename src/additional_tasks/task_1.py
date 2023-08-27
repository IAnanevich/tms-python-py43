# Создать список поездов. Структура словаря: номер поезда, пункт и время прибытия, пункт и время отбытия.
# Вывести все сведения о поездах, время пребывания в пути которых превышает 7 часов 20 минут.

import datetime
from datetime import time
from collections import defaultdict

train_schedule = [
    {'train_number': '632b', 'point_A': 'Grodno', 'start': '00:18', 'point_b': 'Gomel',
     'end': '07:31'},
    # on the way 7h 13m
    {'train_number': '621b', 'point_A': 'Gomel', 'start': '22:05', 'point_b': 'Vitebsk', 'end': '07:37'},
    # on the way 9h 32m
    {'train_number': '632b', 'point_A': 'Brest', 'start': '04:22', 'point_b': 'Mogilev', 'end': '23:25'},
    # on the way 11h 03m
    {'train_number': '632b', 'point_A': 'Grodno', 'start': '07:00', 'point_b': 'Gomel', 'end': '09:50'},
    # on the way 2h 50m
]
dt1 = datetime.timedelta(hours=0, minutes=18)
dt2 = datetime.timedelta(hours=7, minutes=38)
time_train = dt2 -dt1

dt1 = datetime.timedelta(hours=0, minutes=18)
dt2 = datetime.timedelta(hours=7, minutes=31)
way_train = dt2 - dt1
train_schedule[0][('way')] = f'{way_train}'
if time_train < way_train:
    print(train_schedule[0])
    print(f'время в пути {way_train}', '\n')

dt1 = datetime.timedelta(hours=22, minutes=5)
dt2 = datetime.timedelta(hours=7, minutes=37)
way_train = dt2 - dt1
train_schedule[1]['way'] = f'{way_train}'
if way_train > time_train:
    print(train_schedule[1])
    print(f'время в пути {way_train}', '\n')


dt1 = datetime.timedelta(hours=4, minutes=22)
dt2 = datetime.timedelta(hours=23, minutes=25)
way_train = dt2 - dt1
train_schedule[2]['way'] = f'{way_train}'
if way_train > time_train:
    print(train_schedule[2])
    print(f'время в пути {way_train}', '\n')

dt1 = datetime.timedelta(hours=7, minutes=0)
dt2 = datetime.timedelta(hours=9, minutes=50)
way_train = dt2 - dt1
train_schedule[3]['way'] = f'{way_train}'
if way_train > time_train:
    print(train_schedule[3])
    print(f'время в пути {way_train}', '\n')

a = train_schedule[0]
