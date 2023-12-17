# Решить квадратное уравнение вида ax^2 + bx + c = 0.
# Коэффициенты a, b и c вводятся с клавиатуры. Рассмотреть все случаи дискриминанта.

a = float(input('Enter coefficient a: '))  # без проверки на число
b = float(input('Enter coefficient b: '))  # без проверки на число
c = float(input('Enter coefficient c: '))  # без проверки на число

d = b ** 2 - 4 * a * c  # находим дискриминант

if a or b or c:  # не все коэффициенты нулевые
    if a:  # проверка на то, что уравнение квадратное
        if not d:
            print(f'Equation has 1 root: {- b / (2 * a)}')
        elif d > 0:
            print(f'Equation has 2 roots: {(- b + d ** 0.5) / (2 * a)} and {(- b - d ** 0.5) / (2 * a)}')
        else:
            print('Equation has no real roots')
    elif b:  # проверка на то, что уравнение линейное
        print(f'Equation has 1 root: {- c / b}')
else:
    print("it's not an equation, try again")
