# Калькулятор на Python.

def plus(a: int, b: int) -> int:
    """

    :param a: first number
    :param b: second number
    :return: amount "a" and "b"
    """
    return a + b


def minus(a: int, b: int) -> int:
    """

    :param a: first number
    :param b: second number
    :return: subtraction "a" and "b"
    """
    return a - b


def mult(a: int, b: int) -> int:
    """

    :param a: first number
    :param b: second number
    :return: multiplication "a" and "b"
    """
    return a * b


def div(a: int, b: int) -> float:
    """

    :param a: first number
    :param b: second number
    :return: division "a" and "b"
    """
    return a / b


def exp(a: int, b: int) -> int:
    """

    :param a: first number
    :param b: second number
    :return: number a to the power of number b
    """
    return a ** b


while True:
    number_a = input()
    number_b = input()
    if number_a.isdigit() and number_b.isdigit():
        number_a = int(number_a)
        number_b = int(number_b)
        print("1.Сложение")
        print("2.вычитание")
        print("3.умножение")
        print("4.деление")
        print("5.возведение в степень")
        print('6.выход')

    else:
        print('Enter a number')
        break

    choice = input('Выберете число ')
    if choice.isdigit():
        choice = int(choice)

        if choice == 1:
            print(plus(number_a, number_b))
        elif choice == 2:
            print(minus(number_a, number_b))
        elif choice == 3:
            print(mult(number_a, number_b))
        elif choice == 4:
            print(div(number_a, number_b))
        elif choice == 5:
            print(exp(number_a, number_b))
        elif choice == 6:
            break
        else:
            print("Выберете чилсо от 1 до 5")
    else:
        print('Enter a number')
