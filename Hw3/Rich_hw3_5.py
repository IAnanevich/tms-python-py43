# Сделать программу в которой нужно будет угадывать число.
import random
number = random.randint(1,10)
print("Я загадал число, попробуй угадать ")
mode = 1
while mode < 5:
    number_one = int(input("Введи число: "))
    if number_one > number:
        print("Попробуй возьми меньше число")
    elif number_one < number:
        print("Попробуй возьми число побольше")
    else:
        number_one == number
        print(f"Ура, ты угадал! Мое число {number} ")
        break
