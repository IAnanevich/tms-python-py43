# Calc
# 5 функций (+, -, *, /, **) + цикл while как меню с выбором того, что хотим сделать

def my_is_number(dig1: str, dig2: str) -> bool:
    try:
        dig = float(dig1) + float(dig2)
        return dig == dig
    except ValueError:
        return False


def my_add(a_: float, b_: float) -> float:
    return a_ + b_


def my_sub(a_: float, b_: float) -> float:
    return a_ - b_


def my_mult(a_: float, b_: float) -> float:
    return a_ * b_


def my_div(a_: float, b_: float) -> (float, None):
    if not b_:
        return None
    else:
        return a_ / b_


def my_exp(a_: float, b_: float) -> float:
    return a_ ** b_


while 1:
    print("1. Сложить \n2. Отнять \n3. Умножить \n4. Поделить \n5. Х в степень Y")
    choice = input("Любой другой символ - завершить. Что считаем? ")
    aa, bb = 1.2, -5.5
    if choice in ['1', '2', '3', '4', '5']:
        a = input("Число a = ")
        b = input("Число b = ")
        if my_is_number(a, b):
            aa = float(a)
            bb = float(b)
        else:
            print(f"надо было ввести числа, а не {a} и {b}...")
    else:
        break

    if choice == '1':
        print(f'{aa} + {bb} = {my_add(aa, bb)}')
    elif choice == '2':
        print(f'{aa} - {bb} = {my_sub(aa, bb)}')
    elif choice == '3':
        print(f'{aa} * {bb} = {my_mult(aa, bb)}')
    elif choice == '4':
        print(f'{aa} / {bb} = {my_div(aa, bb)}')
    elif choice == '5':
        print(f'{aa} ^ {bb} = {my_exp(aa, bb)}')
