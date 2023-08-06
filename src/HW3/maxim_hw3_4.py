# Решить квадратное уравнение вида ax^2 + bx + c = 0. Коэффициенты a, b и c
# вводятся с клавиатуры. Рассмотреть все случаи дискриминанта.

a, b, c = (int(input("Enter coefficient A of Ax^2 + bx + c = 0: ")),
           int(input("Enter coefficient B of ax^2 + Bx + c = 0: ")),
           int(input("Enter coefficient C of ax^2 + bx + C = 0: ")))
D = b ** 2 - 4 * a * c
if D > 0:
    print(f"{a}x^2{'+' if b>=0 else ''}{b}x{'+' if c>=0 else ''}{c}=0 it has roots "
          f"x1 = {round((-b + D ** 0.5) / (2 * a), 2)}, "
          f"x2 = {round((-b - D ** 0.5) / (2 * a), 2)}")
elif D == 0:
    print(f"{a}x^2{'+' if b>=0 else ''}{b}x{'+' if c>=0 else ''}{c}=0 it has root "
          f"x = {round(-b / (2 * a))}")
else:
    print(f"{a}x^2{'+' if b>=0 else ''}{b}x{'+' if c>=0 else ''}{c}=0 it hasn't root.")
