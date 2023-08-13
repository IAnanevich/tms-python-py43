def decordiv(func):
    def numdiv(num_one, num_two):
        if num_two != 0:
            return func(num_one, num_two)
        else:
            print("division by zero")

    return numdiv


@decordiv
def divide(num_one, num_two):
    return num_one / num_two


x = float(input("Enter one number: "))
y = float(input("Enter two number: "))

divide_result = divide(x, y)
if divide_result is not None:
    print(f"Результат: {divide_result}")
