# calcul
def addition(x: float, y: float) -> float:
    return x + y


def subtraction(x: float, y: float) -> float:
    return x - y


def multiplication(x: float, y: float) -> float:
    return x * y


def division(x: float, y: float) -> float | str:
    if y:
        return x / y
    return 'Нельзя делить на ноль!'


def exponentiation(x: float, y: float) -> float:
    return x ** y


def menu():
    print("Выберите операцию:")
    print("1. Сложение")
    print("2. Вычитание")
    print("3. Умножение")
    print("4. Деление")
    print("5. Возведение в степень")
    print("6. Выход")


while True:
    menu()
    choice = input("Введите номер операции: ")

    if choice == '6':
        print("Выход...")
        break

    try:
        num1 = float(input("Введите первое число: "))
        num2 = float(input("Введите второе число: "))
    except ValueError:
        print("Ошибка! Введите число.")
        continue

    if choice == '1':
        print(num1, "+", num2, "=", addition(num1, num2))
    elif choice == '2':
        print(num1, "-", num2, "=", subtraction(num1, num2))
    elif choice == '3':
        print(num1, "*", num2, "=", multiplication(num1, num2))
    elif choice == '4':
        if num2 == 0:
            print("Ошибка! Деление на ноль невозможно.")
        else:
            print(num1, "/", num2, "=", division(num1, num2))
    elif choice == '5':
        print(num1, "^", num2, "=", exponentiation(num1, num2))
    else:
        print("Неверный ввод! Попробуйте снова.")
