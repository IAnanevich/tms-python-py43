"""Сделать функцию деление чисел и обернуть
декоратором который проверял бы деление на
ноль и отказывал в работе пользователю"""


def carve_decorator(func):
    def inner(*args, **kwargs):
        if not args[1]:
            return "Делить на ноль нельзя "
        return func(*args, **kwargs)

    return inner


@carve_decorator
def div_number(a: float, b: float) -> float:
    """Функция для деления двух чисел.
    :param a: Первое число.
    :param b: Второе число.
    :return: Результат деления."""
    return a / b


while True:
    num_1 = input("Введите первое число:")
    num_2 = input("Введите второе число:")
    if num_1.isdigit() and num_2.isdigit():
        print(div_number(int(num_1), int(num_2)))
        break
    else:
        print("Введите число еще раз!")
