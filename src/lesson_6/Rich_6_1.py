def decordiv(func):
    def numdiv(num_one, num_two):
        """
        :param num_one: one number
        :param num_two: two number
        :return: result / number1,2
        """
        if num_two:
            return func(num_one, num_two)
        else:
            print("division by zero")

    return numdiv


@decordiv
def divide(num_one, num_two):
    """
    :param num_one: num_one/num_two
    :param num_two:
    :return:
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
