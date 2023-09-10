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


def avg(x: str, y: str) -> float | str:
    """

    :param x:
    :param y:
    :return:
    """
    if x.isnumeric() and y.isnumeric():
        x = float(x)
        y = float(y)
        return pow(x * y, 0.5)
    return "Введите положительное число. Числа должны быть положительными и не равняться нулю"


x_1 = input("Введите число x: ")
y_1 = input("Введите число y: ")


try:
    print(avg(x_1, y_1))
except ValueError as error:
    print(error)
