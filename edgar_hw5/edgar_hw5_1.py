# Калькулятор с 5 функциями и циклом.
from typing import Any


def add(x: float, y: float) -> float:
    """ Add two numbers  """
    return x + y


def subtract(x: float, y: float) -> float:
    """Subtract two numbers."""
    return x - y


def multiply(x: float, y: float) -> float:
    """Subtract two numbers."""
    return x * y


def zero_division_check(func):
    """
    A decorator to check division by zero.

    This decorator checks if the divisor is zero before calling the decorated function.

    Args:
        func (callable): The function to be decorated.

    Returns:
        callable: The decorated function that checks for division by zero.
    """

    def wrapper(x: float, y: float) -> str | Any:
        """
        A wrapper function for division with a divide-by-zero check.

        This function checks if the divisor is zero before calling the original division function.

        Args:
        :param x: The dividend.
        :param y: The divisor.
        :return: float: The result of the division if y is not zero, or an error message if y is zero.
        """
        if y == 0:
            return "Error. Division by 0"
        return func(x, y)

    return wrapper


@zero_division_check
def divide(x, y):
    return x / y


def power(x: float, y: float) -> float:
    """
    Calculate the power of a number.
    :param x: Base
    :param y: Exponent
    :return: Result of x raised to the power of y
    """
    return x ** y


while True:
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        continue

    print("Choice operation:")
    print("1. Adding")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Power")
    print("q. Exit")

    choice = input("Enter number operation(1/2/3/4/5/q): ")

    if choice == 'q':
        print("Exit")
        break

    if choice in ('1', '2', '3', '4', '5'):
        choice = int(choice)
        if choice == 1:
            print(f"Result: {add(num1, num2)}")
        elif choice == 2:
            print(f"Result: {subtract(num1, num2)}")
        elif choice == 3:
            print(f"Result: {multiply(num1, num2)}")
        elif choice == 4:
            print(f"Result: {divide(num1, num2)}")
        elif choice == 5:
            print(f"Result: {power(num1, num2)}")
    else:
        print("Wrong operation. Please try again.")
