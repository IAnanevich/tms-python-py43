'''
Решить квадратное уравнение вида ax^2 + bx + c = 0. Коэффициеты a, b и с
вводятся с клавиатуры. Рассмотреть все случаи дискриминанта.
'''

print('Solve a quadratic equation of the form ax^2 + bx + c = 0')
a = int(input('Enter a: '))
b = int(input('Enter b: '))
c = int(input('Enter c: '))

d = b ** 2 - 4 * a * c
if d < 0:
    print('no roots')
elif d == 0:
    print('x=', -b / (2 * a))
else:
    print('x1=', (-b + d ** 0.5) / (2 * a))
    print('x2=', (-b - d ** 0.5) / (2 * a))
