a = int(input("enter a: "))
b = int(input("enter b: "))
import random

number = random.randint(a, b)
number_1 = int(input("enter a number: "))

while number != number_1 :
    if number == number_1 :
        break
    elif number < number_1 :
        print("попробуй меньшее число")
        number_1 = int(input())
    elif number > number_1 :
        print("попробуй большее число")
        number_1 = int(input())
print("ты угадал")
