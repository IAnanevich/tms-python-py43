# Напишите пользовательскую функцию avg(x, y),
# которая должна принимать в качестве аргументов два
# положительных целых или вещественных числа, а возвращать
# их среднее геометрическое (z = pow(x*y, 0.5)).
# В случае передачи недопустимых значений функция
# должна возбуждать исключение ValueError. После того,
# как функция будет готова, используйте ее в скрипте,
# который будет запрашивать у пользователя два числа,
# обрабатывать ввод и выдавать либо среднее геометрическое
# чисел, либо сообщение об ошибке. Для решения задачи
# используйте в теле функции инструкцию raise, а в скрипте try/except.


def avg(x: float, y: float) -> float:
    """

    :param x:
    :param y:
    :return:
    """
    if x > 0 and y > 0:
        return pow(x * y, 0.5)
    else:
        raise ValueError("Числа должны быть положительными и не равняться нулю")


x = float(input("Введите число x: "))
y = float(input("Введите число y: "))

try:
    print(avg(x, y))
except ValueError as error:
    print(error)
