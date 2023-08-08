import random
a = int(input("Введите нижнюю границу : "))
b = int(input("Введите верхнюю границу: "))

number = random.randint(a, b)
number_1 = int(input("Введите ваше число: "))
while number != number_1 :
    if number == number_1 :
        break
    elif number < number_1 :
        print("Ваше число больше загаданного")
    elif number > number_1 :
        print("Ваше число меньше загаданного")
    number_1 = int(input("Введите ваше число: "))
print("Вы угадали число!")