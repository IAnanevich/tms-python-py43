# Напишите пользовательскую функцию avg(x, y), которая должна принимать в качестве аргументов
# два положительных целых или вещественных числа, а возвращать их среднее геометрическое (z = pow(x*y, 0.5)).
# В случае передачи недопустимых значений функция должна возбуждать исключение ValueError.
# После того как функция будет готова, используйте ее в скрипте, который будет запрашивать у пользователя два числа
# обрабатывать ввод и выдавать либо среднее геометрическое чисел, либо сообщение об ошибке.
# Для решения задачи используйте в теле функции инструкцию raise, а в скрипте try/except.
#


def avg(x: str, y: str) -> float:
    """
    find geometric average of two positive numbers if it is possible
    :param x: will be first positive number
    :param y: will be second positive number
    :return: geometric average
    """

    if float(x) > 0 and float(y) > 0:
        return (float(x) * float(y)) ** 0.5
    raise ValueError("Numbers must be positive")


num_1 = input("Enter first positive number: ")
num_2 = input("Enter first positive number: ")

try:
    print(f"Geometric average is: {avg(num_1, num_2)}")
except ValueError as error:
    print(error)
