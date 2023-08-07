#Решить квадратное уравнение вида ax^2 + bx + c = 0.
#Рассмотреть все случаи дискриминанта.
import math

a = float(input("1 odd: "))
b = float(input("2 odd: "))
c = float(input("3 odd: "))
disk = b**2 - 4 * a * c

if disk > 0:
    x1 = (-b + math.sqrt(disk)) / (2 * a)
    x2 = (-b - math.sqrt(disk)) / (2 * a)
    print(f"disk > 0: x1 = {x1}, x2 = {x2}")
elif disk == 0:
    x1 = (-b + math.sqrt(disk)) / (2 * a)
    x2 = (-b - math.sqrt(disk)) / (2 * a)
    print(f"disk = 0: x1 = {x1}, x2 = {x2}")
elif disk < 0:
    print('no roots')



