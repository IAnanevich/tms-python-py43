# Напишите пользовательскую функцию avg(x, y), которая должна принимать в качестве
# аргументов два положительных целых или вещественных числа, а возвращать их среднее
# геометрическое (z = pow(x*y, 0.5)). В случае передачи недопустимых значений функция
# должна возбуждать исключение ValueError. После того как функция будет готова, используйте
# ее в скрипте, который будет запрашивать у пользователя два числа, обрабатывать ввод и
# выдавать либо среднее геометрическое чисел, либо сообщение об ошибке. Для решения
# задачи используйте в теле функции инструкцию raise, а в скрипте try/except.

def avg(x: str, y: str) -> float:
    """
    Return geometric mean of two numbers.
    :param x: positive integers or real numbers
    :param y: positive integers or real numbers
    :return: geometric mean of two numbers
    """
    try:
        x, y = float(x), float(y)
        if x <= 0 or y <= 0:
            raise ValueError("Invalid input")
    except ValueError:
        raise ValueError("Invalid input")
    else:
        return pow(x * y, 0.5)


if __name__ == "__main__":
    value_x, value_y = input("Enter x: "), input("Enter y: ")
    try:
        print(avg(value_x, value_y))
    except ValueError as error:
        print(error)
