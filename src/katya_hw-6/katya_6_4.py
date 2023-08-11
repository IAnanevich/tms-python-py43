# написать декоратор к двум любым функциям,
# который бы считал и выводил время из выполнения
import time
from datetime import datetime

def time_func(func):
    def wrapper(*args):
        start = time.time()
        func(*args)
        finish = time.time()
        print(finish-start)
    return wrapper



@time_func
def div(elem1: float, elem2: float) -> float:
    """
    Calculating the dividing
    :param elem1: first number
    :param elem2: second number
    :return: the dividing the first number by the second numbers
    """
    return elem1 + elem2

elem1 = float(input('Введите значение a: '))
elem2 = float(input('Введите значение b: '))

time_div = div(elem1, elem2)
