# 5.Сделать программу в которой нужно будет угадывать число.

import random
r = random.randint(1, 100)
while True:
    n = int(input('Enter a number:'))
    if r > n:
        print('Add')
    elif r < n:
        print('Reduce')
    else:
        print('You are win!!!')
        break
