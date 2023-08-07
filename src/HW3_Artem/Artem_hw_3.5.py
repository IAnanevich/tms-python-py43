#5. *Сделать программу в которой нужно будет угадывать число.

import random

x = random.randint(1, 100)
n = int(input())

while x:
    if n > x:
        print('меньше')
    elif n < x:
        print("больше")
    elif n == x:
        print('big win')
        break
    n = int(input())

