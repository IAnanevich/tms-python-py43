# Решить квадратное уравнение вида ax^2 + bx + c = 0
# a/b*x^2+x = -c/b

print("Найти Х из:  ax^2 + bx + c = 0")
while 1:
    a = float(input("a = "))
    b = float(input("b = "))
    c = float(input("c = "))
    if a == 0 and b != 0:
        x = -c / b
        print(f"Линейное уравнение:  x = {x}")
    elif a != 0:
        d = b ** 2 - 4 * a * c
        print(f"Дискриминант = {d}")

        if d > 0:
            x1 = (-b + (d**0.5)) / (2 * a)
            x2 = (-b - (d**0.5)) / (2 * a)
            print(f"x1 = {x1} \nx2 = {x2}")
        elif d == 0:
            x = -b / (2 * a)
            print(f"x = {x}")
        else:
            print("нет решения")
    elif c != 0:
        print(f"нет решения,т.к. {c} <> 0 ")
    else:
        print("нет решения,т.к. это все числа мира")
    if input('ещё? (y)') != 'y':
        break
