'''Напишите пользовательскую функцию avg(x, y), которая должна принимать в качестве
аргументов два положительных целых или вещественных числа, а возвращать их среднее
геометрическое (z = pow(x*y, 0.5)). В случае передачи недопустимых значений функция
должна возбуждать исключение ValueError. После того, как функция будет готова, используйте
ее в скрипте, который будет запрашивать у пользователя два числа, обрабатывать ввод
и выдавать либо среднее геометрическое чисел, либо сообщение об ошибке. Для решения
задачи используйте в теле функции инструкцию raise, а в скрипте try/except.'''


def avg(x: float, y: float) -> float:
    """
    The function takes two positive numbers and returns their geometric mean.

    Args:
        x (float): The first number.
        y (float): The second number.

    Returns:
        float: Geometric mean of numbers.

    Raises:
        ValueError: If one of the arguments is a negative number, zero
        TypeError: If one of the arguments is a negative string

    """
    if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
        raise TypeError
    if x <= 0 or y <= 0:
        raise ValueError
    return (x * y) ** 0.5


try:
    x = float(input("Введите первое число: "))
    y = float(input("Введите второе число: "))

    result = avg(x, y)
    print("Среднее геометрическое чисел", x, "и", y, "равно", result)

except (ValueError, TypeError) as e:
    print("Ошибка: Ввод должен быть числом!")
