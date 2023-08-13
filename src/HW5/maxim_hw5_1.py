# Калькулятор на Python - обязательно 5 функций (+, -, *, /, **)
# + цикл while как меню с выбором того, что хотим сделать

def my_sum(a: int | float, b: int | float) -> int | float:
    """
    Return addition of 'a' and 'b'.

    :param a: a number to be added
    :param b: a number to be added
    :return: sum of two numbers
    """
    return a + b


def my_diff(a: int | float, b: int | float) -> int | float:
    """
    Return subtraction of 'a' from 'b'.

    :param a: a number to be subtracted from
    :param b: a number to be subtracted
    :return: difference of numbers
    """
    return a - b


def my_mult(a: int | float, b: int | float) -> int | float:
    """
    Return multiplication of 'a' and 'b'.

    :param a: a number to be multiplied
    :param b: a number to be multiplied
    :return: the result is multiplication
    """
    return a * b


def my_div(a: int | float, b: int | float) -> float:
    """
    Return division of 'a' by 'b'.

    :param a: a number divisible by
    :param b: a divisor of the number
    :return: division result
    """
    return a / b


def my_pow(a: int | float, b: int | float) -> int | float:
    """
    Return 'a' raised to the power of 'b'.

    :param a: a number raised to a power
    :param b: the power of the number
    :return: a number 'a' to a power of 'b'
    """
    return a ** b


if __name__ == '__main__':
    first_number = int(input("Enter a first number: "))
    second_number = int(input("Enter a second number: "))
    while 1:
        input_user = input("Choose operation:\n 1 is +\n 2 is -\n 3 is *\n 4 is /\n 5 is **\n other is exit\n-> ")
        match input_user:
            case '1':
                print(f"{first_number} + {second_number} = {my_sum(first_number, second_number)}\n")
            case '2':
                print(f"{first_number} - {second_number} = {my_diff(first_number, second_number)}\n")
            case '3':
                print(f"{first_number} * {second_number} = {my_mult(first_number, second_number)}\n")
            case '4':
                print(f"{first_number} / {second_number} = {my_div(first_number, second_number)}\n")
            case '5':
                print(f"{first_number} ^ {second_number} = {my_pow(first_number, second_number)}\n")
            case _:
                break
