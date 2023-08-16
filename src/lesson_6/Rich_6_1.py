def decordiv(func: callable) -> callable:
    def numdiv(num_one: float, num_two: float) -> float:
        """
        :param num_one: one number
        :param num_two: two number
        :return: result / number1,2
        """
        if num_two:
            return type(func(num_one, num_two))
        else:
            print("division by zero")
            print(type)

    return numdiv


@decordiv
def divide(num_one: float, num_two: float) -> float:
    """
    :param num_one:
    :param num_two:
    :return: num_one/num_two
    """
    return num_one / num_two


try:
    x = float(input("Enter one number: "))
    y = float(input("Enter two number: "))
except ValueError:
    print("Invalid input. Please enter valid numbers.")
else:
    divide_result = divide(x, y)
    if divide_result is not None:
        print(f"Результат: {divide_result}")
