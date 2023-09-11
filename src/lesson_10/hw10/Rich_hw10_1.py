"""Напишите пользовательскую функцию avg(x, y), которая должна принимать в качестве
аргументов два положительных целых или вещественных числа, а возвращать их среднее
геометрическое (z = pow(x*y, 0.5)). В случае передачи недопустимых значений функция
должна возбуждать исключение ValueError.
После того, как функция будет готова, используйте
ее в скрипте, который будет запрашивать у пользователя два числа, обрабатывать ввод
и выдавать либо среднее геометрическое чисел, либо сообщение об ошибке. Для решения
задачи используйте в теле функции инструкцию raise, а в скрипте try/except."""


from typing import Union


def avg(x: Union[int, float], y: Union[int, float]):
    """
    Функция вычисляет среднее геометрическое двух чисел.

    :param x: one num
    :param y: two num
    :return:
    :raises ValueError: x, y = note +
    """
    if x <= 0 or y <= 0:
        raise ValueError("Num positive.")
    return (x * y) ** 0.5


try:
    x = float(input("Enter one num: "))
    y = float(input("Enter two num: "))

    result = avg(x, y)
    print(f"Среднее геометрическое чисел {x} и {y} равно {result:.2f}")
except ValueError as e:
    print(f"Error: {e}")
except Exception as e:
    print(f"Error: {e}")
