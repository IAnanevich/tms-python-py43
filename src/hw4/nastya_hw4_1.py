"""Калькулятор на Python
5 функций (+, -, *, /, **) + цикл while как меню с выбором того, что хотим сделать"""


def add(a, b):
    return a+b


def minus(a, b):
    return a-b


def mul(a, b):
    return a*b


def div(a, b):
    return a/b


def con(a, b):
    return a**b


while True:
    n = input('What do you want (* , /,  +,  -,  ** )? enter q for exit : ')
    if n == 'q':
        print('Bye')
        break
    elif n != '+' and n != '-' and n != '*' and n != '/' and n != '**':
        print('Try again(')
        continue
    first_number = int(input('Enter a '))
    second_number = int(input('Enter b '))
    if n == '*':
        print(mul(first_number, second_number))
    elif n == '/':
        print(div(first_number, second_number))
    elif n == '-':
        print(minus(first_number, second_number))
    elif n == '+':
        print(add(first_number, second_number))
    else:
        print(con(first_number, second_number))
