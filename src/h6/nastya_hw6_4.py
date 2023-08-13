"""4. Написать декоратор к 2-м любым функциям, который бы считал и выводил время
их выполнения. Подсказка: from datetime import datetime time = datetime.now()"""
import time
from datetime import datetime


def dec(fun):
    def wrapper(i):
        fun(i)
        print(datetime.strftime(datetime.now(), '%Y-%m-%d %H:%M:%S'))
    return wrapper
# декоратор надо документировать? как писать аннотацию и надо ли?


@dec
def exa(n: int) -> list:
    """
    year month day at the moment but 2 seconds apart
    :param n: number
    :return:year month day as many times as the number with a difference of 2 seconds
    """
    return [datetime.now(time.sleep(2)) for i in range(n)]


@dec
def fact(n: int) -> int:
    """
    Finding degree in degree
    :param n: num
    :return: num in degree number in degree number
    """
    return n ** n ** n


fact(5)
exa(3)
