# Написать декоратор к 2-м любым функциям, который бы считал и выводил время
# их выполнения. Подсказка from datetime import datetime time = datetime.now()
from datetime import datetime


def check(func):
    def execution_time(*args):
        time_start = datetime.now()
        f = func(*args)
        print(datetime.now() - time_start)
        return f
    return execution_time


@check
def ver_1(ls: list) -> dict:
    """
    Return dict where the keys are the list items and the value is the number of their repetitions

    :param ls: list for processing
    :return: dict where the keys are the list items and the value is the number of their repetitions
    """
    _dict = dict()
    for i in ls:
        _dict[i] = _dict.get(i, 0) + 1
    return _dict


@check
def ver_2(ls: list) -> dict:
    """
    Return dict where the keys are the list items and the value is the number of their repetitions

    :param ls: list for processing
    :return: dict where the keys are the list items and the value is the number of their repetitions
    """
    return {i: ls.count(i) for i in set(ls)}


if __name__ == "__main__":
    my_list = range(10000000)
    ver_1(my_list)
    ver_2(my_list)
