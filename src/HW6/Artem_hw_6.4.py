# Сделать функцию деление чисел и обернуть декоратором который проверял бы деление на ноль
# и отказывал в работе пользователю

import time
from datetime import datetime


def dekor(func):
    def div(a, b):
        if b != 0:
            return func(a, b)
        else:
            print('Enter number more than zero')

    return div


@dekor
def say(a, b):
    """
    dividing a by b
    :param a: first_number
    :param b: second_number
    :return: dividing a by b
    """
    return a / b


a = input("Enter first number: ")
b = input("Enter second number: ")
if a.isdigit() and b.isdigit():
    print(say(float(a), float(b)))
else:
    print('Enter a number')
