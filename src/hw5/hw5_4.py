# Сделать функцию, которая отдает время с задержкой в 1 сек
# Сделать функцию, генератор списков
# Количество элементов списка задает пользователь

import time
from _datetime import datetime


def generate_list(how_many_iems: int = 10) -> list:
    """
    Сгенерирует новый лист
    :param how_many_iems: length of list
    :return: new list
    """
    result = []
    for i in range(1, how_many_iems + 1):
        result.append(get_time())
    return result


def get_time() -> str:
    """
    С задержкой в 1 секунду выренет текущее время строкай вида "%d-%m-%Y %H:%M:%S"
    :return: время строкай вида "%d-%m-%Y %H:%M:%S"
    """
    time.sleep(1)
    return datetime.strftime(datetime.now(), "%d-%m-%Y %H:%M:%S")


print("\nPlease enter length of new list, greater then 0 and less then 11")
length = int(input("Input here: "))
if length > 10 or length < 1:
    print(generate_list())
else:
    print(generate_list(length))
