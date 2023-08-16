"""Калькулятор на Python
5 функций (+, -, *, /, **) + цикл while как меню с выбором того, что хотим сделать"""


def add(a: int, b: int) -> int:
    """
    Adding 2 numbers
    :param a: first_number
    :param b: second_number
    :return: summa first_number and second_number
    """
    return a + b


def minus(a: int, b: int) -> int:
    """
    Subtracting 2 numbers
    :param a: first_number
    :param b: second_number
    :return: subtraction first_number and second_number
    """
    return a - b


def mul(a: int, b: int) -> int:
    """
    Multiplying 2 numbers
    :param a: first_number
    :param b: second_number
    :return: multiplication first_number by the second_number
    """
    return a * b


def div(a: int, b: int) -> float:
    """
    Dividing 2 numbers
    :param a: first_number
    :param b: second_number
    :return: division first_number by the second_number
    """
    if b == 0:
        return "You can't divide by zero"
    return a / b


def con(a: int, b: int) -> int:
    """
    Degree 2 numbers
    :param a: first_number
    :param b: second_number
    :return: degree conversion first_number by the second_number
    """
    return a ** b


while True:
    n = input('What do you want (* , /,  +,  -,  ** )? enter q for exit : ')
    if n == 'q':
        print('Bye')
        break
    elif n not in ['+', '-', '*', '/', '**']:
        print('Try again(')
        continue
    try:
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
    except ValueError:
        print('Try again(')
