# Калькулятор на Python (+, -, *, /, **).  с циклом while


def sum_numbers(a: float, b: float) -> float:
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
    if b == 0:
        result = print('Делить на ноль нельзя')
    else:
        result = print(a / b)
    return result


def expon(a: float, b: float) -> float:
    """
    Calculating the exponentiation
    :param a: first number
    :param b: second number
    :return: the exponentiation of the first number by the second numbers
    """
    return a ** b


while True:
    a = input('Введите переменную а: ')
    b = input('Введите переменную b: ')
    print(' 0: Выход из программы \n','1: Операция сложения: a + b \n','2: Операция вычитания: a - b \n',
        '3: Операция умножения: a * b \n','4: Операция деления: a / b\n','5: Операция возведения в степень: a ** b ')
    d = input('Выберите номер необходимого действия: ')

    if a.isdigit() and b.isdigit() and d.isdigit():
        a = float(a)
        b = float(b)
        d = float(d)

        if d == 0:
            break
        elif d == 1:
            sum_numbers(a, b)
        elif d == 2:
            diff(a, b)
        elif d == 3:
            mult(a, b)
        elif d == 4:
            div(a, b)
        elif d == 5:
            expon(a, b)
        else:
            print('Введите номер, соотвествующий, необходимой операции!')
            break
    else:
        print('Введите числовые значения')
