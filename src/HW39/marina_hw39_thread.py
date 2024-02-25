# Создать программу, которая добавляет в список числа от 0 до 10000.
#
# b. С помощью потоков

from threading import Thread
import time

make_list = []


def add_list_element(elem: int) -> None:
    """
    added element in list
    :param elem: element for add
    :return: None
    """
    make_list.append(elem)


def make_array_thread(n: int) -> float:
    """
    returned work time of add n elements in list by threads
    :param n: length of list
    :return: work time
    """
    start_time = time.time()
    threads = [Thread(target=add_list_element, args=(i,)) for i in range(n)]
    # стартуем все потоки
    for thread in threads:
        thread.start()
    # ждем окончания всех потоков
    for thread in threads:
        thread.join()
    work_time = time.time() - start_time
    return work_time
