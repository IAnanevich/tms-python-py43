# Создать список поездов. Структура словаря: номер поезда, пункт и время
# прибытия, пункт и время отбытия. Вывести все сведения о поездах, время
# пребывания в пути которых превышает 7 часов 20 минут.
from datetime import datetime, timedelta


def find_more_on_the_way(trains, days: int = 0, hours: int = 0, minutes: int = 0) -> list:
    """ Find trains that are on the way longer than the specified time.

    :param trains: list of dictionaries with trains
    :param days: quantity of days
    :param hours: quantity of hours
    :param minutes: quantity of minutes
    :return: list of dictionaries
    """
    return [train for train in trains
            if train['end'] - train['start'] > timedelta(days=days, hours=hours, minutes=minutes)]


if __name__ == "__main__":
    list_of_trains = [
        {
            "number": "52",
            "point_A": "Brest",
            "start": datetime(2023, 8, 23, 14, 12),
            "point_B": "St. Peterburg",
            "end": datetime(2023, 8, 24, 8, 6)
             },
        {
            "number": "714",
            "point_A": "Minsk",
            "start": datetime(2023, 8, 23, 19, 53),
            "point_B": "Vitebsk",
            "end": datetime(2023, 8, 23, 23, 8)
            },
        {
            "number": "631",
            "point_A": "Minsk",
            "start": datetime(2023, 8, 24, 15, 18),
            "point_B": "Grodno",
            "end": datetime(2023, 8, 24, 19, 10)
            },
        {
            "number": "680",
            "point_A": "Grodno",
            "start": datetime(2023, 8, 23, 11, 58),
            "point_B": "Vitebsk",
            "end": datetime(2023, 8, 23, 22, 39)
            }
    ]
    for lst in find_more_on_the_way(list_of_trains, hours=7, minutes=20):
        print(f"Train №{lst['number']}: {lst['point_A']} to {lst['point_B']}")
