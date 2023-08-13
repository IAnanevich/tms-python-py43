"""
Написат декоратор Функция принимает бым функциям который бы считал и выводил время бы считал и выводил время
их выполнения. Подсказка: выполнения
"""
from datetime import datetime
from functools import wraps


def decorator(func):
    @wraps(func)
    def wrapper():
        start_time = datetime.now()
        func()
        run_time = datetime.now() - start_time
        print(f"Функция {func.__name__} выполняется - {run_time}")
    return wrapper

@decorator
def sum_while():
    sum = i = 0
    while i < 10000000:
        sum += i
        i += 1

@decorator
def sum_for():
    sum = 0
    for i in range(0, 10000000):
        sum += i

sum_while()
sum_for()
