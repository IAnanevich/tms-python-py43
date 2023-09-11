"""Сделать свое исключение и подключить к try/except"""
from typing import Union


class MyCustomException(Exception):
    def __init__(self, message):
        super().__init__(message)


def divide(a: Union[int, float], b: Union[int, float]):
    """
    :param a: num one
    :param b: num two
    :return: div
    """
    if b == 0:
        raise MyCustomException("/ 0 error")
    return a / b


try:
    x = float(input("Enter one num: "))
    y = float(input("Enter two num: "))

    result = divide(x, y)
    print(f"result div {x} на {y} равен {result}")
except MyCustomException as e:
    print(f"Error: {e}")
except ValueError:
    print("Error - is not a number")
except Exception as e:
    print(f"Error: {e}")
