# Написать декоратор к 2-м любым функциям, который бы считал и выводил время
# их выполнения.


from datetime import datetime
import time
from memory_profiler import profile


def check_time(func):
    def wrapper():
        start = datetime.now()
        func()
        print(f'time: {datetime.now()-start}')

    return wrapper


def check_time_v2(func):
    def wrapper():
        start = time.time()
        func()
        print(f'time: {time.time()-start}')

    return wrapper


@profile
@check_time
@check_time_v2
def func_1():
    (tuple(filter(lambda x: x[::-1] == x, ('1121', '1221', '939', '0193910'))))


@profile
@check_time
@check_time_v2
def func_2():
    (lambda x: print('чётное') if (x % 2 == 0) else print('нечётное'))(999)


if __name__ == '__main__':
    func_1()
    func_2()
