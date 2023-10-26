# Создать генератор геометрической прогрессии
from typing import Generator


def generator(number_1: int | float, number_2: int | float) -> Generator[int | float, None, None]:
    """
    Geometric progression generator
    :param number_1: number_1
    :param number_2: number_2
    :return: generator of numbers
    """
    for i in range(10):
        yield number_1 * (number_2 ** i)
