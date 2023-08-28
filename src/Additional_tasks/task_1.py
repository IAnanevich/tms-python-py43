# Создать список поездов. Структура словаря: номер поезда, пункт и время
# прибытия, пункт и время отбытия. Вывести все сведения о поездах, время
# пребывания в пути которых превышает 7 часов 20 минут.
# Пример:
# list_of_trains = [
# {"number": "", "point_A": “", "start": "",
# "point_B": "", "end": ""},
# …
# ]
# =================================================================================================================

from datetime import datetime, timedelta
from typing import List, Dict, Any

# List of trains
list_of_trains = [
    {"number": "123", "point_A": "City_A", "start": "10:00", "point_B": "City_B", "end": "19:30"},
    {"number": "456", "point_A": "City_C", "start": "08:15", "point_B": "City_D", "end": "11:45"},
    {"number": "789", "point_A": "City_E", "start": "17:30", "point_B": "City_F", "end": "21:31"},
    {"number": "852", "point_A": "City_B", "start": "09:00", "point_B": "City_E", "end": "22:32"},
    # .... add more trains to the list
]


def get_duration(departure_time: str, arrival_time: str) -> timedelta:
    """
    Calculate the duration of the train journey.
    :param departure_time: Departure time in format "HH:MM".
    :param arrival_time: Arrival time in format "HH:MM".
    :return: timedelta: Duration of the journey as a timedelta object.
    """
    departure = datetime.strptime(departure_time, "%H:%M")
    arrival = datetime.strptime(arrival_time, "%H:%M")
    return arrival - departure


def main() -> None:
    """
    Print information about trains with journey duration exceeding 7 hours and 20 minutes.
    """

    threshold = timedelta(hours=7, minutes=20)

    for train in list_of_trains:
        duration = get_duration(train['start'], train['end'])

        if duration > threshold:
            print(f"Train {train['number']} travels for {duration}")
            print(f"Departure: {train['start']} from {train['point_A']}")
            print(f"Arrival: {train['end']} at {train['point_B']}\n")


if __name__ == "__main__":
    main()
