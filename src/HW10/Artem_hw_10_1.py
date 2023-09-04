from math import sqrt


def avg(x, y):
    """
    compares x and y
    :param x:
    :param y:
    :return: their geometric mean
    """
    if x < 0 or y < 0:
        raise ValueError('the number must not be negative')
    return sqrt(x * y)


n = float(input('Enter first number: '))
m = float(input('Enter second number: '))

try:
    print(f'geometric mean: {avg(n, m)}')
except ValueError as error:
    print(error)
