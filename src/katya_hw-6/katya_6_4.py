# написать декоратор к двум любым функциям,
# который бы считал и выводил время их выполнения
import time


def time_func(func):
    def wrapper(*args):
        start = time.time()
        func(*args)
        finish = time.time()
        print(finish - start)
    return wrapper


@time_func
def sum(elem1: float, elem2: float) -> float:
    """
    Calculating the sum
    :param elem1: first number
    :param elem2: second number
    :return: the sum of first number and second numbers
    """
    return elem1 + elem2


@time_func
def exp(a: float, b: float) -> float:
    """
    Calculating the exponentiation
    :param a: first number
    :param b: second number
    :return: the exponentiation of the first number by the second numbers
    """
    return a ** b


elem1 = float(input('Введите значение a: '))
elem2 = float(input('Введите значение b: '))

time_sum = sum(elem1, elem2)
time_exp = exp(elem1, elem2)
