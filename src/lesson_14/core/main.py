# import my_test.test_1 as t1
# import my_test.test_2 as t2


from my_test.test_1 import func_test_1

from my_test.test_2 import *

# from .my_test.test_2 import func_test_2


# 1. Именнованные (абсолютные) - from my_test.test_1 import func_test_1
# 2. Неименнованные (относительные) - from .my_test.test_2 import func_test_2


# func_test_1()
# func_test_2()
# func_2_test_2()


class Main:
    name = 'Petr'

    def __init__(self, name=None):
        self.name = name

    def print_name(self):
        print(f'hello {self.name}')

    @classmethod
    def print_name_class(cls):
        print(f'hello {cls.name}')

    @staticmethod
    def print_text():
        print('hello')


main = Main('Dima')
main.print_name()
main.print_name_class()
main.print_text()
