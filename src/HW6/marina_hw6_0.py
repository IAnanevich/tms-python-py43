# Сделать функцию деление чисел и обернуть декоратором который проверял бы деление на ноль
# и отказывал в работе пользователю


def div_decorator(func):
    def inner(*args, **kwargs):
        if not args[1]:
            return "Division by zero is not defined"
        return func(*args, **kwargs)

    return inner


@div_decorator
def div_number(a: float, b: float) -> float:
    """
    divide first number to second number
    :param a: first number
    :param b: second number
    :return: division resul first and second number
    """
    return a / b


while True:
    num_1 = input("Enter first number:")
    num_2 = input("Enter second number:")
    if (
        num_1.isdigit() and num_2.isdigit()
    ):  # проверка на число, ждем получения целых чисел
        print(div_number(int(num_1), int(num_2)))
        break
    else:
        print("You need to enter number, try again")
