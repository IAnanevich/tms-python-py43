# Калькулятор с 5 функциями и циклом.

def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    if y == 0:
        return "Error: Division by 0 "
    return x / y


def power(x, y):
    return x ** y


while True:
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
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print("Result:", add(num1, num2))
        elif choice == '2':
            print("Result:", subtract(num1, num2))
        elif choice == '3':
            print("Result:", multiply(num1, num2))
        elif choice == '4':
            print("Result:", divide(num1, num2))
        elif choice == '5':
            print("Result:", power(num1, num2))
    else:
        print("Wrong operation. Please try again.")
