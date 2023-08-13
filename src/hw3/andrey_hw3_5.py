'''
Сделать программу в которой нужно будет угадывать число
используйте рандом
import random
number = random.randint(1,100)
промежуток должен быть задан через input
также добавьте подсказку, которая будет писать
число загаданное больше или меньше
например
программа загадала число 20
вы вводите 50
программа отвечает: увы, мое загаданное число меньше
'''

import random
from typing import Tuple

while True:
    interval_ = input('Enter the interval of integers (Example:1,100): ')
    interval_ = interval_.split(',')
    if len(interval_) != 2:
        print('Error: Incorrect interval')
        continue
    try:
        interval_start,interval_end = int(interval_[0]),int(interval_[1])
    except:
        print('Error: Incorrect interval')
        continue

    if interval_start < interval_end:
        break
    else:
        print('Error: Incorrect interval')
        continue

print(f'Guess the number from {interval_start} to {interval_end}!')
r = random.randrange(interval_start, interval_end)
n = 0
while (n := int(input('Enter numbers:')) or n == 0) and n != r:
    if n > r:
        print(f'Alas, my number is more than')
    else:
        print(f'Alas, my number is less than')
else:
    print('Guessed!!!')
