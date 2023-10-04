# В массиве целых чисел с количеством элементов 19 определить максимальное
# число и заменить им все четные по значению элементы. Использовать рандом для
# заполнения цикла элементами, диапазон рандома принимать от пользователя.
from random import randint


def gen_list_and_proc(start: int, end: int) -> list:
    """ Generates a list and returns a list in which even numbers are replaced by the maximum element.

    :param start: start random range
    :param end: end random range
    :return: a list where even numbers are replaced by the maximum element
    """
    gen_list = [randint(start, end) for i in range(1, 20)]
    max_elem = max(gen_list)
    return list(map(lambda x: x if x % 2 else max_elem, gen_list))


if __name__ == "__main__":
    begin, finish = input("Enter start of random's: "), input("Enter end of random's: ")
    try:
        begin, finish = int(begin), int(finish)
        if begin > finish:
            raise ValueError
    except TypeError as error:
        print(error)
    print(gen_list_and_proc(begin, finish))
