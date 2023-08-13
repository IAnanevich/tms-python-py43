# Cделать функцию которая будет вызываться из генератора списков и по запросу
# к ней отдавать текущее время с задержкой в 1 сек. Кол-во элементов нового списка
# n запрашивать у пользователя. Пример сгенерированного списка из 4-х элементов:
# ['2022-01-26 11:43:46', '2022-01-26 11:43:47', '2022-01-26 11:43:48', '2022-01-26 11:43:49']
from datetime import datetime, timedelta


def delay(sec: int) -> str:
    """
    Return datetime style string

    :param sec: number of seconds in the period
    :return: the current time is longer by the specified number of seconds
    """
    return datetime.strftime(datetime.now() + timedelta(seconds=sec), '%Y-%m-%d %h:%M:%S')


def gen_list(length: int) -> list:
    """
    Return a list of datetime style string

    :param length: list length
    :return: a list of the range with a difference per second
    """
    return [delay(i) for i in range(length)]


if __name__ == '__main__':
    print(gen_list(int(input("Enter the number of items in the list: "))))
