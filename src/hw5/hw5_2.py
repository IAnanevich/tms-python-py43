"""
нахождение факториала
"""
n = int(input("Введите n: "))

fact = 1
for i in range(1, n + 1):
    fact *= i

print(fact)

# способ с функцией
def calc_factorial(n: int) -> int:
    if n == 1:
        return 1
    return calc_factorial(n - 1) * n

print(calc_factorial(n))
