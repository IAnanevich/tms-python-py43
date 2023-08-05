from typing import Union, Any, Callable

# шаблон
# def имя_функции(параметр_1, параметр_2, ...):
#     код
#     return переменная(ые) / (ничего) / None / без return


def summa(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    """
    Add a to b
    :param a: first number
    :param b: second number
    :return: sum of 2 numbers
    """
    return a + b


def mult(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    """

    :param a:
    :param b:
    :return:
    """
    return a * b


def increase_list(numbers: Any, func: Callable) -> list:
    """

    :param numbers:
    :return:
    """
    new_numbers = []
    for i in numbers:
        new_numbers.append(i + 1)

    return new_numbers


print(mult(2, 3.2))
