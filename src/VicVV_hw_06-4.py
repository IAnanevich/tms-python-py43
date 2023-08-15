# Написат декоратор который бы считал и выводил время выполнения.

from datetime import datetime
from functools import wraps


def deco_time(func):
    @wraps(func)
    def wrapper(*args):
        time_start = datetime.now()
        f = func(*args)
        print(f'время выполнения {datetime.now() - time_start}')
        return f
    return wrapper


@deco_time
def my_is_number(dig1: str) -> bool:
    try:
        float(dig1)
        return True
    except ValueError:
        return False


@deco_time
def my_add(a: float, b: float) -> float:
    while 1:
        input("длинная пауза...?")
        break
    return a + b


x = 33.33
y = 55.55
print(f'{x} is number? {my_is_number(x)}')
print(f'{x} + {y} = {my_add(x, y)}')
