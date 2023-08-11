# Найти факториал числа N.
# Определяется как произведение всех натуральных чисел от 1 до N включительно
# Реализовать рекурсивной функцией

def factorial_function(number: int) -> int:
    """
    Calculating the factorial of a number
    :param number: any natural number
    :return: result of calculation number!
    """
    if number > 1:
        return number * factorial_function(number-1)
    return 1


print("\nPlease enter any natural number N to calc N!")
# try to convert
try:
    n = int(input("Input here: "))
except ValueError as e:
    print(f"N = 0, because of {e}")
    n = 0

if n == 0:
    print(f"{n}! = 1")
elif n > 0:
    print(f"{n}! = {factorial_function(n)}")
else:
    print(f"Wrong input! N={n} is not natural number")
