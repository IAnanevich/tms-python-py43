# Сделать программу в которой нужно будет угадывать число
# Используйте рандом
import random

n = random.randint(1, 100)
print("\nЗагадано случайное число от 1 до 100. Угадай какое")
some_value = input('>> ')
if some_value.isdigit():
    x = int(some_value)
else:
    x = n = 0

while x != n:
    if n > x:
        print("\nЗагадано число больше чем ", x)
    else:
        print("\nЗагадано число меньше чем ", x)

    print("Новая попытка")
    some_value = input('>> ')
    if some_value.isdigit():
        x = int(some_value)
    else:
        x = n = 0

if x == 0:
    print("\nПолный провал!")
    print("Попробуй еще раз и вводи число!")
else:
    print("\nBingo!!!")
    print("Загаданное число это ", x)
