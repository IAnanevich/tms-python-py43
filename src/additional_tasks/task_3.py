# Для заданного числа N составьте программу вычисления суммы
# S=1+1/2+1/3+1/4+...+1/N, где N – натуральное число.


def some_calc(number: int) -> float:
    """
    Вычисление: S = 1 + 1 / 2 + 1 / 3 + 1 / 4 + ... + 1 / N
    :param number: Это N
    :return: Результат вычисления
    """
    result = 0
    for i in range(1, number + 1):
        result += 1 / i
    return result


some_input = input("Натуральное число >>")
try:
    n = int(some_input)
    n = max(n, -n, 1)
except ValueError:
    print("Получится в следующий раз...")
    n = -1

if n > 0:
    # S = 1 + 1 / 2 + 1 / 3 + 1 / 4 + ... + 1 / N
    print(f"\nN = {n}, S = 1 + 1 / 2 + 1 / 3 + 1 / 4 + ... + 1 / N = {some_calc(n)}")
