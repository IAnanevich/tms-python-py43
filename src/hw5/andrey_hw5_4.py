# Сделать функцию, которая будет вызываться из генератора списков,
# по запросу к ней отдавать текущее время с задержкой в 1 секунду.
# Количество элементов нового списка запрашивать у пользователя.
from datetime import datetime
from time import sleep


def delayed_time() -> datetime:
    """
    returns the current time with a delay of 1 second
    :return:
    """
    sleep(1)
    return datetime.now()


try:
    len_list = int(input('Enter length of list: '))
except ValueError:
    len_list = 0

print([datetime.strftime(delayed_time(), '%Y-%m-%d %H:%M:%S') for i in range(len_list)])
