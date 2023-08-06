# Сделать программу в которой нужно будет угадывать число

import random

number_r = random.randint(1,100)
number = 0
while number != number_r:
    number = int(input('введите предпологаемое число '))
    if number > number_r:
        print(f'число должно быть меньше {number}')
    elif number < number_r:
        print(f'число должно быть больше {number}')
    else:
        print(f'вы угадали число')
        break
