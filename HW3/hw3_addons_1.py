# Решить квадратное уравнение вида ax^2 + bx + c = 0.
# Коэффициеты a, b и с
# Вводятся с клавиатуры.
# Рассмотреть все случаи дискриминанта.

print("\nРешаем квадратное уравнение вида ax^2 + bx + c = 0")

print("\nВведите A")
some_value = input('>> ')
try:
    a = int(some_value)
except ValueError:
    print("Ясно... пусть будет A = 1")
    a = 1

print("\nВведите B")
some_value = input('>> ')
try:
    b = int(some_value)
except ValueError:
    print("Ясно... пусть будет B = 4")
    b = 4

print("\nВведите C")
some_value = input('>> ')
try:
    c = int(some_value)
except ValueError:
    print("Ясно... пусть будет C = 2")
    c = 2

print(f"\nРешаем квадратное уравнение {a}x^2 + {b}x + {c} = 0")
dis = b ** 2 - 4 * a * c
if dis < 0:
    print('Нет корней')
elif dis == 0:
    print('Есть один корень при x=', -b / (2 * a))
else:
    print("Есть два корня")
    print('x1=', (-b + dis ** 0.5) / (2 * a))
    print('x2=', (-b - dis ** 0.5) / (2 * a))
