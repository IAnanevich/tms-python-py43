# Написать декоратор к 2-м любым функциям, который бы считал и выводил время их выполнения.

from datetime import datetime


def time_decorator(func):

    def inner(*args, **kwargs):
        time_start = datetime.now()
        func(*args, **kwargs)
        print(f'Function {func.__name__} has worked {datetime.now() - time_start}')

    return inner


@time_decorator
def make_power(a: int, b: int) -> int:
    """
    exponentiation number "a" in power b
    :param a: base
    :param b: degree
    :return: power result
    """
    return a ** b


@time_decorator
def do_factorial(n: int) -> int:
    """
    get factorial of number
    :param n: base
    :return: factorial of number n
    """
    res = 1
    for i in range(1, n + 1):
        res *= i
    return res


# получение времени работы функций
make_power(9, 33333)
do_factorial(4444)
