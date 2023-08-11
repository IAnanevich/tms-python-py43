'''Решить квадратное уравнение вида ax^2+bx+c=0
Коэффициенты a,b,c вводятся с клавиатуры .
Рассмотреть все случаи дискриминанта.'''

import math

a = float(input("Введите коэффициент a: "))
b = float(input("Введите коэффициент b: "))
c = float(input("Введите коэффициент c: "))
discriminant = b ** 2 - 4 * a * c
if discriminant > 0:
    print("Уравнение имеет два корня:")
    print("x1 =", (-b + math.sqrt(discriminant)) / (2 * a))
    print("x2 =", (-b - math.sqrt(discriminant)) / (2 * a))
elif discriminant == 0:
    print("Уравнение имеет один корень:")
    print("x =", -b / (2 * a))
else:
    print("Нет корней")
