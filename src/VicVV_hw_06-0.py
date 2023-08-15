# 1) Сделать функцию деление чисел и обернуть декоратором
# который проверял бы деление на ноль и отказывал в работе пользователю - обяз
from functools import wraps


def deco_f1(func):

    @wraps(func)
    def wrapper(*args):
        if args[1] == 0:
            print("делить на 0 нельзя")
            return None
        else:
            return func(*args)
    return wrapper


@deco_f1
def my_div(dig1, dig2):
    return dig1 / dig2


x = 33.33
y = 0
print(f'{x} / {y} = {my_div(x, y)}')
