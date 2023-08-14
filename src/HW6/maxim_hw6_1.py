# Сделать функцию деление чисел и обернуть декоратором который
# проверял бы деление на ноль и отказывал в работе пользователю

def check(func):
    def div_by_0(*args):
        try:
            return func(*args)
        except ZeroDivisionError:
            return "Denied execution!"
    return div_by_0


@check
def my_div(a: int | float, b: int | float) -> float:
    """
    Return division of 'a' by 'b'.

    :param a: a number divisible by
    :param b: a divisor of the number
    :return: division result
    """
    return a / b


if __name__ == "__main__":
    print(my_div(int(input("Enter an integer a: ")), int(input("Enter an integer b: "))))
