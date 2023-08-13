# Калькулятор на Python - обязательно
# 5 функций (+, -, *, /, **) + цикл while как меню с выбором того,
def division(a: int, b: int) -> float | None:
    """
     divides a by b
    :param a: numerator
    :param b: denominator
    :return: None when divided by 0
    """
    if b == 0:
        print('division by 0')
        return None
    return a / b


def multiplication(a: int, b: int) -> int:
    """
     multiplication a by b
    :param a: multipliers 1
    :param b: multipliers 2
    :return:
    """
    return a * b


def degree(a: int, b: int) -> int:
    """
     degree a in b
    :param a: number
    :param b: degree
    :return:
    """
    return a ** b


def sum(a: int, b: int) -> int:
    """
     addition of two numbers
    :param a: number 1
    :param b: number 2
    :return:
    """
    return a + b


def difference(a: int, b: int) -> int:
    """
     difference of two numbers
    :param a: reduced
    :param b: subtracted
    :return:
    """
    return a - b


def error_check(int_x):
    try:
        return int(int_x)
    except ValueError:
        print('entered not an integer, enter = 0')
        return 0


options = {1: sum, 2: difference, 3: multiplication, 4: division, 5: degree}
header = 'Choose an action:\n0 - Exit\n1 - Addition\n2 - Subtraction\n3 - Multiplication\n4 - Division\n5 - Degree'
print(header)
while choice := error_check(input('your choice: ')):
    if choice > 5:
        print('wrong choice, try again, ', end="")
        continue

    a = error_check(input('Enter integer a: '))
    b = error_check(input('Enter integer b: '))

    print(f'={options.get(choice)(a, b)}')
    print(header)
