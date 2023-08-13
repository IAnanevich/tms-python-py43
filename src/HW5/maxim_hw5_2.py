# Написать программу для нахождения факториала. Факториал натурального числа
# n определяется как произведение всех натуральных чисел от 1 до n включительно.
# Реализацию выполнить в виде рекурсивной функции.

def factorial(x: int) -> int:
    """
    Find x!.

    :param x: factorial of this number
    :return: factorial of x
    """
    return x * factorial(x-1) if x != 0 else 1


if __name__ == '__main__':
    print(factorial(int(input("Enter a non-negative integer: "))))
