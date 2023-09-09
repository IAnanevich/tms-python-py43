# Сделать функцию, которая будет вызываться из генератора списков,
# по запросу к ней отдавать текущее время с задержкой в 1 секунду.
# Количество элементов нового списка запрашивать у пользователя.

from datetime import datetime, timedelta


def make_time_list(n: int) -> list[str]:
    return [datetime.strftime(datetime.now() + timedelta(seconds=i), '%Y-%m-%d %H:%M:%S') for i in range(n)]


while True:
    len_list = input('Enter length of list: ')
    if len_list.isdigit():
        times_list = [c for c in make_time_list(int(len_list))]
        print(times_list)
        break
    else:
        print('You need to enter integer-number of length, try again)')
