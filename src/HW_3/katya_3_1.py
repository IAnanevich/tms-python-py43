# Решить квадратное уравнение. Коэффициенты вводятся с клавиатуры.

a = int(input('введите коэффициент а='))
b = int(input('введите коэффициент b='))
c = int(input('введите коэффициент c='))

d = b**2-4*a*c
if d == 0:
    print(f'x = {( -b / 2*a )}')
elif d > 0:
    print(f'x1 = {(((-b) - (d**(1/2))) / (2*a))} и x2 = {( ((-b) + (d**(1/2))) / (2*a))}')
else:
    print(f'корней нет')
