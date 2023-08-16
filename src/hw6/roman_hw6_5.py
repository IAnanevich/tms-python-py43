"""Написать декоратор к 2-м любым функциям, который бы считал и выводил
время их выполнения. Подсказка: from datetime import datetime, time = datetime.now()"""
from datetime import datetime
import time


def execution_time_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = datetime.now()
        result = func(*args, **kwargs)
        print(f"Время выполнения функции {func.__name__}: {(datetime.now() - start_time).total_seconds()} секунд")
        return result

    return wrapper


@execution_time_decorator
def function1():
    time.sleep(2)
    print("Функция 1 выполнена")


@execution_time_decorator
def function2():
    time.sleep(3)
    print("Функция 2 выполнена")


function1()
function2()
