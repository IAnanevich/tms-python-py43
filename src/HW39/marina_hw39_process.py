# Создать программу, которая добавляет в список числа от 0 до 10000.
#
# c. С помощью процессов

import multiprocessing
import time

my_list = []


def add_list_elements(start_elem: int, end_elem) -> None:
    """
    added elements in list
    :param start_elem: first element for add
    :param end_elem: last element for add
    :return: None
    """
    for elem in range(start_elem, end_elem):
        my_list.append(elem)


def make_array_process(n: int) -> float:
    """
    returned work time of add n elements in list by processes
    :param n: length of list
    :return: work time
    """
    num_processes = 4
    work_per_process = n // num_processes
    start_time = time.time()
    processes = [
        multiprocessing.Process(
            target=add_list_elements, args=(i, i + work_per_process)
        )
        for i in range(0, n, work_per_process)
    ]
    # стартуем все процессы
    for process in processes:
        process.start()
    # ждем окончания всех процессов
    for process in processes:
        process.join()
    end_time = time.time() - start_time
    return end_time
