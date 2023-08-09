# Сделать функцию, которая будет вызываться из генератора списков,
# по запросу к ней отдавать текущее время с задержкой в 1 секунду.
# Количество элементов нового списка запрашивать у пользователя.

from datetime import datetime, timedelta


def make_time_list(n: int) -> list[str]:
    return [datetime.strftime(datetime.now() + timedelta(seconds=i), '%Y-%m-%d %H:%M:%S') for i in range(n)]


len_list = int(input('Enter length of list: '))
times_list = [c for c in make_time_list(len_list)]
print(times_list)
