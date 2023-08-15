# Calc
# 5 функций (+, -, *, /, **) + цикл while как меню с выбором того, что хотим сделать

def my_is_number(dig1: str, dig2: str) -> bool:
    try:
        dig1 = float(dig1)
        dig2 = float(dig2)
        return True
    except ValueError:
        return False


def my_add(a: float, b: float) -> float:
    return a + b


def my_sub(a: float, b: float) -> float:
    return a - b


def my_mult(a: float, b: float) -> float:
    return a * b


def my_div(a: float, b: float) -> (float, None):
    if b == 0:
        return None
    else:
        return a / b


def my_exp(a: float, b: float) -> float:
    return a ** b


while 1:
    print("1. Сложить \n2. Отнять \n3. Умножить \n4. Поделить \n5. Х в степень Y")
    choice = input("Любой другой символ - завершить. Что считаем? ")

    if choice in ['1', '2', '3', '4', '5']:
        a = input("Число a = ")
        b = input("Число b = ")
        if my_is_number(a, b):
            a = float(a)
            b = float(b)
        else:
            print(f"надо было ввести числа, а не {a} и {b}...")
            a = 1.2
            b = -5.5
    else:
        break

    if choice == '1':
        print(f'{a} + {b} = {my_add(a, b)}')
    elif choice == '2':
        print(f'{a} - {b} = {my_sub(a, b)}')
    elif choice == '3':
        print(f'{a} * {b} = {my_mult(a, b)}')
    elif choice == '4':
        print(f'{a} / {b} = {my_div(a, b)}')
    elif choice == '5':
        print(f'{a} ^ {b} = {my_exp(a, b)}')
