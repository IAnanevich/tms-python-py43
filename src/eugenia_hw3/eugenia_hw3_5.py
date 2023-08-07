import random
a = int(input("enter a: "))
b = int(input("enter b: "))

number = random.randint(a, b)
number_1 = int(input("enter a number: "))
while number != number_1 :
    if number == number_1 :
        break
    elif number < number_1 :
        print("попробуй меньшее число")
    elif number > number_1 :
        print("попробуй большее число")
    number_1 = int(input("enter a number: "))
print("ты угадал")
