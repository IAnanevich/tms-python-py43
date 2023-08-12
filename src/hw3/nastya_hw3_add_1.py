"""Решить квадратное уравнение вида ax^2 + bx + c = 0. Коэффициеты a, b и с
вводятся с клавиатуры. Рассмотреть все случаи дискриминанта."""

import math
a = int(input('Enter the number before x^2: '))
b = int(input('Enter the number before x: '))
c = int(input('Enter the number without x ans x^2: '))
if b ** 2 - 4 * a * c > 0:
    print(f'First root: {(- b + math.sqrt(b ** 2 - 4 * a * c)) / (2 * a)}')
    print(f'Second root: {(- b - math.sqrt(b ** 2 - 4 * a * c)) / (2 * a)}')
elif b ** 2 - 4 * a * c == 0:
    print(f'Root: {- b / 2 * a}')
else:
    print('No roots')
