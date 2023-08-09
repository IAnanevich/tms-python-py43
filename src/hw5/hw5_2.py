# Найти факториал числа N.
# Определяется как произведение всех натуральных чисел от 1 до N включительно
# Реализовать рекурсивной функцией

def factorial_function(number: int) -> int:
    """
    :param number: any natural number
    :return: result of calculation number!
    """
    if number > 1:
        return number * factorial_function(number-1)
    else:
        return 1


print("\nPlease enter any natural number N to calc N!")
n = int(input("Input here: "))

if n == 0:
    print(f"{n}! = 1")
elif n > 0:
    print(f"{n}! = {factorial_function(n)}")
else:
    print("Wrong input!")
