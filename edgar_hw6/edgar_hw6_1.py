# Сделать функцию деление чисел и обернуть декоратором который проверял бы
# деление на ноль и отказывал в работе пользователю
# ---------------------------------------------------------------------------------------------------------------

def zero_division_check(func):
    """
    A decoder to check division by zero.
    """
    def wrapper(a: float, b: float) -> float:
        """
        A wrapper function for division with a divide-by-zero check.
        :param a: Divisible
        :param b: Divisor
        :return: Result of division
        """
        try:
            result1 = func(a, b)
            return result1
        except ZeroDivisionError as e:
            return e

    return wrapper


@zero_division_check
def divide(a: float, b: float) -> float:
    """
    The function of dividing two numbers.
    :param a: Divisible
    :param b: Divisor
    :return: Result of division
    """
    return a / b


# Example
while True:
    try:
        num1 = float(input("Enter first num: "))
        num2 = float(input("Enter second num: "))
        break
    except ValueError as error:
        print(error)

print("Result: ", num1/num2)
