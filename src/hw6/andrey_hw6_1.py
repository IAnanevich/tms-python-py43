# Сделать функцию деление чисел и обернуть декоратором который проверял бы деление на ноль
# и отказывал в работе пользователю
from functools import reduce
from andrey_hw6_6 import isnumber


def decor(func):
    def check(args: tuple) -> float:
        """
        null check
        :type args: object
        """
        if 0 in args:
            print('Error: zero division')
            return 0.0
        return func(args)

    return check


@decor
def division(args: tuple) -> float:
    """
    executes the division example
    :param args:
    :return:
    """
    return reduce(lambda a, x: a / x, args, 1)


if __name__ == '__main__':
    while True:
        example = input('Enter division example: ').replace(' ', '').split("/")
        if len(example) < 2:
            print('example not correct')
            continue
        example = tuple(map(isnumber, example))
        if None in example:
            print('example not correct')
            continue
        print(division(example))
        break
