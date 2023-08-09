'''Сделать функцию которая будет вызываться из генератора списков и по запросу
к ней отдавать текущее время с задержкой в 1 секунду. Количество элементов нового
списка n запрашивать у пользователя. Пример сгенерированного списка из 5 элементов:
['2022-01-26 11:43:46', '2022-01-26 11:43:47', '2022-01-26 11:43:48', '2022-01-26 11:43:49', '2022-01-26 11:43:50'].'''
from datetime import datetime, timedelta
import time


def generate_time_list(n):
    current_time = datetime.now()
    time_list = []
    for _ in range(n):
        time_list.append(datetime.strftime(current_time, '%Y-%m-%d %H:%M:%S'))
        current_time += timedelta(seconds=1)
        time.sleep(1)
    return time_list


n = int(input("Введите количество элементов списка: "))
result = generate_time_list(n)
print(result)
