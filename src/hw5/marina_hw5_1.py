# Калькулятор на Python - обязательно
# 5 функций: +,'-', *, /, ** + цикл while как меню с выбором того, что хотим сделать


def add_number(a: float, b: float) -> float:
    return a + b


def minus_number(a: float, b: float) -> float:
    return a - b


def mult_number(a: float, b: float) -> float:
    return a * b


def div_number(a: float, b: float) -> float | str:
    if b:
        return a / b
    return 'Division by zero is not possible'


def get_power(a: float, b: float) -> float:
    return a ** b


print('Welcome to Python calculator! Please enter your numbers')

while True:
    print('\n What do you want to do?')
    print('1. Addition', '2. Subtraction', '3. Multiplication', '4. Division', '5. Power', '0. Exit', sep='\n')
    action = input('Please enter operation:')
    if action.isdigit():
        action = int(action)
        if action == 0:
            print('Goodbye!')
            break
        elif 0 < action < 6:
            first_number = float(input('First number is: '))  # полагаю, что тут строку не введут
            second_number = float(input('Second number is: '))  # полагаю, что тут строку не введут
            if action == 1:
                print(f'Addition result is: {add_number(first_number, second_number)}')
            elif action == 2:
                print(f'Subtraction result is: {minus_number(first_number, second_number)}')
            elif action == 3:
                print(f'Multiplication result is: {mult_number(first_number, second_number)}')
            elif action == 4:
                print(f'Division result is: {div_number(first_number, second_number)}')
            elif action == 5:
                print(f'Power result is: {get_power(first_number, second_number)}')
        else:
            print('You need to enter number 1 - 5, or 0 for Exit, try again')
    else:
        print('You need to enter integer NUMBER to choose operation not String, try again')
