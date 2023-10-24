"""Напишите пользовательскую функцию avg(x, y), которая должна принимать в качестве аргументов
два положительных целых или вещественных числа, а возвращать их среднее геометрическое (z = pow(x*y, 0.5)).
В случае передачи недопустимых значений функция должна возбуждать исключение ValueError. После того, как функция
будет готова, используйте ее в скрипте, который будет запрашивать у пользователя два числа, обрабатывать ввод и
выдавать либо среднее геометрическое чисел, либо сообщение об ошибке. Для решения задачи используйте в теле
функции инструкцию raise, а в скрипте try/except."""


def avg(x: int | float, y: int | float) -> float:
    """
    Multiplies 2 numbers and then puts that number under the root
    :param x: x
    :param y: y
    :return: (x * y) ** 0.5
    """
    if x <= 0 or y <= 0:
        raise ValueError('first and second number must be positive number')
    return (x * y) ** 0.5


try:
    first_number = float(input('Enter first number: '))
    # можно написать 2 или больше типов перед input, чтобы input ждал несколько типов?
    second_number = float(input('Enter second number: '))
    print(avg(x=first_number, y=second_number))
except Exception as error:
    print(error)
