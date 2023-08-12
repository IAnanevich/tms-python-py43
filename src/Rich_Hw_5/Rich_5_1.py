def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Деление на 0"


def decorator_test(func):
    def calculate():
        print("Выберите операцию:")
        print("1. Сложение")
        print("2. Вычитание")
        print("3. Умножение")
        print("4. Деление")
        print("5. Выход")


        choice = input("Введите номер операции (1/2/3/4/5): ")

        if choice == '5':
            print("Выход из программы")
            return
        elif choice in ('1', '2', '3', '4'):
            num1 = float(input("Введите первое число: "))
            num2 = float(input("Введите второе число: "))
            result = func(num1, num2, choice)
            print(f"Результат операции: {result}")
        else:
            print("Неправильный ввод")
            return
    return calculate


@decorator_test
def calculate(x, y, choice):
    if choice == '1':
        return add(x, y)
    elif choice == '2':
        return subtract(x, y)
    elif choice == '3':
        return multiply(x, y)
    elif choice == '4':
        return divide(x, y)


calculate()
