#calc
def plus(a, b):
    return a + b


def minus(a, b):
    return a - b


def umnozh(a, b):
    return a * b


def delit(a, b):
    return a / b


def exp(a, b):
    return a ** b


print("Выберите операцию:")
print("1. Сложение")
print("2. Вычитание")
print("3. Умножение")
print("4. Деление")
print("5. Возведение в степень")

operation = input(" 1/2/3/4/5: ")

num1 = int(input("Введите первое число: "))
num2 = int(input("Введите второе число: "))

if operation == '1':
    print(num1, "+", num2, "=", plus(num1, num2))
elif operation == '2':
    print(num1, "-", num2, "=", minus(num1, num2))
elif operation == '3':
    print(num1, "*", num2, "=", umnozh(num1, num2))
elif operation == '4':
    print(num1, "/", num2, "=", delit(num1, num2))
elif operation == '5':
    print(num1, "**", num2, "=", exp(num1, num2))
else:
    print("Неверный ввод")
