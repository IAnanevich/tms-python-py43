# Сделать программу в которой нужно будет угадывать числа

import random
d = input("диапазон угадайки: ")
if d.isdigit():
    number = random.randint(1, int(d))
    while 1:
        o = int(input(f"угадайка (от 1 до {d}) :"))
        if o > number:
            print("надо меньше")
        elif o < number:
            print("надо больше")
        else:
            print(f"УРА! я загадал {number}")
            break
else:
    print("это не число")
