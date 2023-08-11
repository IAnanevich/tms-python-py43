# Калькулятор на Python (+, -, *, /, **).  с циклом while


def sum(a: float, b: float) -> float:
    """
    Calculating the sum
    :param a: first number
    :param b: second number
    :return: the sum of the first and second numbers
    """
    return a + b


def diff(a: float, b: float) -> float:
    """
    Calculating the difference
    :param a: first number
    :param b: second number
    :return: the difference between the first and second numbers
    """
    return a - b


def mult(a: float, b: float) -> float:
    """
    Calculating the multiplication
    :param a: first number
    :param b: second number
    :return: the multiplication of the first and second numbers
    """
    return a * b


def div(a: float, b: float) -> float:
    """
    Calculating the dividing
    :param a: first number
    :param b: second number
    :return: the dividing the first number by the second numbers
    """
    return a / b


def exp(a: float, b: float) -> float:
    """
    Calculating the exponentiation
    :param a: first number
    :param b: second number
    :return: the exponentiation of the first number by the second numbers
    """
    return a ** b


while True:
    a = float(input('Введите переменную а: '))
    b = float(input('Введите переменную b: '))
    print(' 0: Выход из программы \n','1: Операция сложения: a + b \n','2: Операция вычитания: a - b \n',
        '3: Операция умножения: a * b \n','4: Операция деления: a / b\n','5: Операция возведения в степень: a ** b ')
    d = int(input('Выберите номер необходимого действия: '))

    if d == 0:
        break
    elif d == 1:
        result = sum(a, b)
        print(result)
    elif d == 2:
        result = diff(a, b)
        print(result)
    elif d == 3:
        result = mult(a, b)
        print(result)
    elif d == 4:
        if b == 0:
            print('Делить на ноль нельзя')
        else:
            result = div(a, b)
            print(result)
    elif d == 5:
        result = exp(a, b)
        print(result)
else:
    print('Введите номер, соотвествующий, необходимой операции!')
