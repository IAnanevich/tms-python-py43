"""Сделать функцию которая будет вызываться из генератора списков и
по запросу к ней отдавать текущее время с задержкой в 1 сек.
Кол-во элементов нового списка п запрашивать у пользователя.
Пример сгенерированного списка из 5-и элементов:
['2022-01-26 11:43:46', '2022-01-26 11:43:47', '2022-01-26 11:43:48', '2022-01-26 11:43:49']
Подсказка: вывод текущего времени в определённом формате:
from datetime import datetime   datetime.strftime(datetime.now(), '%Y-%m-%d %H:%M:%S')"""

from datetime import datetime
import time

n = int(input('How many times?: '))
print([datetime.strftime(datetime.now(time.sleep(1)), '%Y-%m-%d %H:%M:%S') for i in range(n)])
