# Создать список поездов.
# Структура словаря: номер поезда, пункт и время прибытия, пункт и время отбытия.
# Вывести все сведения о поездах, время пребывания в пути которых превышает 7 часов 20 минут.
# Пример:
# list_of_trains = [
# {"number": "", "point_A": “", "start": "",
# "point_B": "", "end": ""},
# …
# ]


def print_longer_then(trains: list, hours: int, minutes: int) -> None:
    """
    Выведет все сведения о поездах, время пребывания в пути которых превышает X часов Y минут
    :param trains: Список поездов для анализа
    :param hours: Время пребывания в пути в часах
    :param minutes: Время пребывания в пути в минутах
    :return: None
    """

    # Сколько всего минут во времени для проверки
    total_minutes = hours * 60 + minutes

    # Проверяем список поездов
    for train in trains:

        # Разобъем время отбытия на составляющие
        start = str(train["start"]).split(sep=":")

        # Время отбытия в минутах с начала дня
        start_time = int(start[0]) * 60 + int(start[1])

        # Разобъем время прибытия на составляющие
        end = str(train["end"]).split(sep=":")

        # Время прибытия в минутах с начала дня
        end_time = int(end[0]) * 60 + int(end[1])

        # Можем прибыть и в этом и в следующем дне
        if end_time >= start_time:
            # Текущий день
            travel_time = end_time - start_time
        else:
            # Следующий день
            travel_time = (24 * 60 - int(start[0]) * 60 - int(start[1])) + end_time

        # Проверка на главное условие: время пребывания в пути которых превышает
        if travel_time > total_minutes:
            print(train)


# Наш список поездов (https://pass.rw.by/)
list_of_trains = [
    {"number": "1", "point_A": "Minsk", "point_B": "Moscow", "start": "16:00", "end": "22:55"},
    {"number": "2", "point_A": "Minsk", "point_B": "Piter", "start": "17:36", "end": "09:52"},
]

# Наша обработка списка
print_longer_then(trains=list_of_trains, hours=7, minutes=20)
