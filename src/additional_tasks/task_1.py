# Создать список поездов. Структура словаря: номер поезда, пункт и время прибытия, пункт и время отбытия.
# Вывести все сведения о поездах, время пребывания в пути которых превышает 7 часов 20 минут.
# Пример: # list_of_trains = [# {"number": "", "point_A": "", "start": "",# "point_B": "", "end": ""},# …#]

from datetime import datetime


def choice_train(train_start: str, train_end: str) -> bool:
    """
    check if train is in road more than 7:20
    :param train_start: departure time
    :param train_end: arrival time
    :return: bool value if train is in road more than 7:20
    """
    # преобразовываем значения времени отправки и прибытия для работы с ними
    # разность между временем прибытия и отправления(м.б отрицательной)
    time_sec = (
        datetime.strptime(train_end, "%H:%M") - datetime.strptime(train_start, "%H:%M")
    ).total_seconds()
    # реальное время в пути
    road_time_sec = time_sec if time_sec > 0 else 24 * 60 * 60 - time_sec
    return road_time_sec > (7 * 60 + 20) * 60


list_of_trains = [
    {
        "number": 8,
        "point_A": "Brest",
        "start": "17:37",
        "point_B": "Moscow",
        "end": "06:56",
    },
    {
        "number": 51,
        "point_A": "St. Petersburg",
        "start": "18:05",
        "point_B": "Brest",
        "end": "11:56",
    },
    {
        "number": 7,
        "point_A": "Moscow",
        "start": "22:17",
        "point_B": "Brest",
        "end": "10:15",
    },
    {
        "number": 6105,
        "point_A": "Minsk",
        "start": "05:22",
        "point_B": "Molodechno",
        "end": "07:08",
    },
    {
        "number": 705,
        "point_A": "Polotsk",
        "start": "07:08",
        "point_B": "Mogilev",
        "end": "08:27",
    },
    {
        "number": 147,
        "point_A": "Minsk",
        "start": "00:07",
        "point_B": "Kaliningrad",
        "end": "10:38",
    },
]

# пробегаемся по списку и выводим информацию только по тем, кто в пути более 7:20
for train in list_of_trains:
    if choice_train(train_start=str(train["start"]), train_end=str(train["end"])):  # без str ругается MyPy
        print(train)
