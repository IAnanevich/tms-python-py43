# список из дат +1 секунду
from datetime import timedelta, datetime


def get_time(i: float) -> float:
    return datetime.strftime(datetime.now() + timedelta(seconds=i), '%Y-%m-%d %H:%M:%S')

num = input("Введите n: ")

if num.isdigit():
    num = int(num)
    data = [get_time(i) for i in range(1, num + 1)]
    print(data)
else:
    print("Число некорректное")
