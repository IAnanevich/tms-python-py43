# calc
while True:
    print("Меню:")
    print("1. Сложение (+)")
    print("2. Вычитание (-)")
    print("3. Умножение (*)")
    print("4. Деление (/)")
    print("5. Возведение в степень (**)")
    print("6. Выход")
    choice = input("Выберите операцию (1-6): ")
    if choice == "6":
        print("Выход из программы...")
        break
    num1 = float(input("Введите первое число: "))
    num2 = float(input("Введите второе число: "))
    if choice == "1":
        result = num1 + num2
        print(f"Результат сложения: {result}")
    elif choice == "2":
        result = num1 - num2
        print(f"Результат вычитания: {result}")
    elif choice == "3":
        result = num1 * num2
        print(f"Результат умножения: {result}")
    elif choice == "4":
        if num2 != 0:
            result = num1 / num2
            print(f"Результат деления: {result}")
        else:
            print("Ошибка! Деление на ноль.")
    elif choice == "5":
        result = num1 ** num2
        print(f"Результат возведения в степень: {result}")
    else:
        print("Некорректный выбор операции. Попробуйте снова.")
print()
