# Сделать функцию, которая будет вызываться из генератора списков,
# по запросу к ней отдавать текущее время с задержкой в 1 секунду.
# Количество элементов нового списка запрашивать у пользователя
from datetime import datetime
import time


def list_numbers(n) -> list[str]:
    """гениратор списка"""
    new_list = []
    for i in range(1, n + 1):
        new_list.append(datetime.strftime(datetime.now(time.sleep(1)), '%Y-%m-%d %H:%M:%S'))
    return new_list


number = input('enter the length of the list: ')
if number.isdigit():
    number = int(number)
    print(list_numbers(number))
else:
    print('Enter a number')
