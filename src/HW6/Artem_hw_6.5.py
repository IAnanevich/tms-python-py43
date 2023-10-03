#Написать декортаор к 2-м любым функция, который бы считал и выводил время их выполнения

import time
from datetime import datetime

def list_numbers(func):

    def wrapper(*args):
        start = time.time() # begin point
        func()
        end = time.time() - start # code time
        print(end)
        return end
    return wrapper


@list_numbers
def say(a=5, b=4) -> int:
    """
    adding numbers
    :param a: first number
    :param b: second number
    :return: amount first number and second number
    """
    return a + b


@list_numbers
def day(x = 1):
    """
    list generator
    :param x: max value in the list
    :return: listing
    """
    new_list = []
    for i in range(1,x):
        new_list.append(datetime.strftime(datetime.now(time.sleep(1)), '%Y-%m-%d %H:%M:%S'))
    return new_list


say()
day()
