# Создать программу, которая добавляет в список числа от 0 до 10000.
#
# a. без потоков и процессов

import time

my_list = []


def add_list_element(elem: int) -> None:
    """
    added element in list
    :param elem: element for add
    :return: None
    """
    my_list.append(elem)


def make_array_regular(n: int) -> float:
    """
    returned work time of add n elements in list
    :param n: length of list
    :return: work time
    """
    start_time = time.time()
    for i in range(n + 1):
        add_list_element(i)
    work_time = time.time() - start_time
    return work_time
