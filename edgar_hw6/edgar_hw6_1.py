# Сделать функцию деление чисел и обернуть декоратором который проверял бы
# деление на ноль и отказывал в работе пользователю
# ---------------------------------------------------------------------------------------------------------------

def zero_division_check(func):
    def wrapper(a, b):
        if b == 0:
            return "Error: division by 0"
        return func(a, b)

    return wrapper


@zero_division_check
def divide(a, b):
    return a / b


# Example
num1 = float(input("Enter first num: "))
num2 = float(input("Enter second num: "))

result = divide(num1, num2)
print("Result: ", result)
