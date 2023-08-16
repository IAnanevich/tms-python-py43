from typing import Union


def add(x: float, y: float) -> float:
    """
    :param x:
    :param y:
    :return: x sum y
    """
    return x + y


def subtract(x: float, y: float) -> float:
    """
    :param x:
    :param y:
    :return: x minus y
    """
    return x - y


def multiply(x: float, y: float) -> float:
    """
    :param x:
    :param y:
    :return: x multiply y
    """
    return x * y


def division(x: float, y: float) -> float:
    """
    :param x:
    :param y:
    :return: x division y
    """
    if y != 0:
        return x / y


def decorator_test(func):
    """
    :param func:
    :return: operation
    """
    def calc():
        print("Выберите операцию:")
        print("1. Сложение")
        print("2. Вычитание")
        print("3. Умножение")
        print("4. Деление")
        print("5. Выход")

        choice: str = input("Введите номер операции (1/2/3/4/5): ")

        if choice == '5':
            print("Выход из программы")
            return
        elif choice in ('1', '2', '3', '4'):
            num1_input = input("Введите первое число: ")
            num2_input = input("Введите второе число: ")
            try:
                num1: float = float(num1_input)
                num2: float = float(num2_input)
            except ValueError:
                print("Введено не число")
                return

            result: Union[float, str] = func(num1, num2, choice)
            print(f"Результат операции: {result}")
        else:
            print("Неправильный ввод")
            return

    return calc


@decorator_test
def calculate(x: float, y: float, choice) -> float:
    if choice == '1':
        return add(x, y)
    elif choice == '2':
        return subtract(x, y)
    elif choice == '3':
        return multiply(x, y)
    elif choice == '4':
        return division(x, y)


calculate()
