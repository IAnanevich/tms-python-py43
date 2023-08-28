"""Пользователь вводит два числа n и х.
Нужно вывести на экран число х ровно n раз в формате [х, х, … , х]. """

n = int(input('Enter how many times to repeat: '))
x = input('Enter what to repeat: ')
print('[', end='')
for b in range(n-1):
    print(f'{x}, ', end='')
print(f'{x}', end='')
print(']')
