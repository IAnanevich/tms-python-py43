# Сделать функцию, которая будет вызываться из генератора списков и по запросу к ней отдавать текущее время с задержкой
# в 1 сек. Количество элементов нового списка n запрашивать у пользователя. Пример сгенерированного списка из 5-и
# элементов: ['2022-01-26 11:43:46', '2022-01-26 11:43:47', '2022-01-26 11:43:48', '2022-01-26 11:43:49']
# Подсказка: вывод текущего времени в определенном формате:
# from datetime import datetime
# datetime.strftime(datetime.now(), '%Y-%m-%d $H:%M:%S')

from datetime import datetime
import time


def get_current_time_with_delay():
    time.sleep(1)  # delay 1 sec
    current_time = datetime.now()
    return current_time.strftime('%Y-%m-%d %H:%M:%S')


def generator_time_list(n):
    time_list = []
    for _ in range(n):
        time_list.append(get_current_time_with_delay())
    return time_list


# Get the number of list items from the user

n = int(input("Enter the number of items in the list: "))

# Generate a list of items with delay and output the result

time_list = generator_time_list(n)
print("Generate list: ", time_list)
