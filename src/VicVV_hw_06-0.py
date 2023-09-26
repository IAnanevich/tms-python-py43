# 1) Сделать функцию деление чисел и обернуть декоратором
# который проверял бы деление на ноль и отказывал в работе пользователю - обяз
from functools import wraps
from typing import Callable, Any


def deco_f1(func) -> Callable[[tuple[Any, ...]], Any | None]:
    @wraps(func)
    def wrapper(*args):
        if args[1] == 0:
            print("делить на 0 нельзя")
            return None
        return func(*args)

    return wrapper


@deco_f1
def my_div(dig1: int | float, dig2: int | float) -> float:
    """
    Result of division of two numbers
    :param dig1:first number
    :param dig2:second number
    :return: division first by second
    """
    return dig1 / dig2


x = 33.33
y = 66.4

print(f"{x} / {y} = {my_div(x, y)}")
