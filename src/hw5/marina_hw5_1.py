# Калькулятор на Python - обязательно
# 5 функций: +,'-', *, /, ** + цикл while как меню с выбором того, что хотим сделать


def add_number(a: float, b: float) -> float:
    return a + b


def minus_number(a: float, b: float) -> float:
    return a - b


def mult_number(a: float, b: float) -> float:
    return a * b


def div_number(a: float, b: float) -> float:
    return a / b


def get_power(a: float, b: float) -> float:
    return a ** b


print('Welcome to Python calculator! Please enter your numbers')

while True:
    print('\n What do you want to do?')
    print('1. Addition', '2. Subtraction', '3. Multiplication', '4. Division', '5. Power', '0. Exit', sep='\n')
    action = int(input('Please enter operation:'))
    if action == 0:
        break
    elif 0 < action < 6:
        first_number = float(input('First number is: '))
        second_number = float(input('Second number is: '))
        if action == 1:
            print(add_number(first_number, second_number))
        elif action == 2:
            print(minus_number(first_number, second_number))
        elif action == 3:
            print(mult_number(first_number, second_number))
        elif action == 4:
            if second_number:
                print(div_number(first_number, second_number))
            else:
                print('Division by zero is not possible')
        elif action == 5:
            print(get_power(first_number, second_number))
    else:
        print('You need to enter number 1 - 5, or 0 for Exit, try again')
