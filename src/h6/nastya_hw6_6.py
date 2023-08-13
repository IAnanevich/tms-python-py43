"""Сделать функцию деление чисел и обернуть декоратором который проверял бы
деление на ноль и отказывал в работе пользователю"""


def dec(fun):
    def wrapper(a, b):
        if b != 0:
            print(fun(a, b))
        else:
            print("You can't divide by zero")
    return wrapper


@dec
def div(a: int, b: int) -> float:
    """
    Dividing 2 numbers
    :param a: first_number
    :param b: second_number
    :return: division first_number by the second_number
    """
    return a/b


div(51, 0)
