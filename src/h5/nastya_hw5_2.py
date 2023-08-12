"""Написать программу для нахождения факториала. Факториал натурального числа п определяется
как произведение всех натуральных чисел от 1 до п включительно. Реализацию выполнить в виде
рекурсивной функции. """


def fact(n: int) -> int:
    """
    Recursion to find the factorial
    :param n: number
    :return: factorial of a number
    """
    if n == 0:
        return 1
    elif n < 0:
        return 'None'
    return n * fact(n - 1)


try:
    number = int(input('Enter number for factorial: '))
    print(fact(number))
except ValueError:
    print('Try again')
