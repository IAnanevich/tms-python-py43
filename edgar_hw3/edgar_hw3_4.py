# Решить квадратное уравнение вида ax^2 + bx + c = 0. Коэффициенты a, b и
# вводятся с клавиатуры. Рассмотреть все случаи дискриминанта.

def solve_quadratic_equation(a, b, c):
    if a == 0:
        return "Коэффициент а не может быть равен 0"
    discriminant = b ** 2 - 4 * a * c

    if discriminant > 0:
        x1 = (-b + discriminant ** 0.5) / (2 * a)
        x2 = (-b - discriminant ** 0.5) / (2 * a)
        return x1, x2
    elif discriminant == 0:
        x = -b / (2 * a)
        return x
    else:
        return "Уравнение не имеет действительных коренй"


# Enter data
a = float(input('Введите а не равен 0: '))
b = float(input("Введите b: "))
c = float(input("Введите с: "))

roots = solve_quadratic_equation(a, b, c)

print("Корни квадратного уравнения: ", roots)
