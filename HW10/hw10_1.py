# 3) Напишите пользовательскую функцию avg(x, y)
# которая должна принимать в качестве аргументов два положительных целых или вещественных числа
# а возвращать их среднее геометрическое (z = pow(x*y, 0.5)).
# В случае передачи недопустимых значений функция должна возбуждать исключение ValueError.
#
# После того, как функция будет готова, используйте ее в скрипте,
# который будет запрашивать у пользователя два числа,
# обрабатывать ввод и выдавать либо среднее геометрическое чисел, либо сообщение об ошибке.
# Для решения задачи используйте в теле функции инструкцию raise, а в скрипте try/except.

def check(s: str) -> bool:
    """
    Можно ли привести строку к float
    :param s: строка
    :return: да или нет
    """
    try:
        float(s)
        return True
    except ValueError:
        return False


def avg(x: str, y: str) -> float:
    """
    Возвращает среднее геометрическое двух чисел
    :param x: first number
    :param y: second number
    :return: return average value of 2 number
    """
    if check(x) and check(y):
        return (float(x) + float(y)) / 2
    raise ValueError("Недопустимое значение Х или У")


input_x = input("Enter number x: ")
input_y = input("Enter number y: ")

try:
    print(avg(x=input_x, y=input_y))
except ValueError as err:
    print(err)
