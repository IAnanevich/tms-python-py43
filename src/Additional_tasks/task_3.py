# Для заданного числа N составьте программу вычисления суммы
# S=1+1/2+1/3+1/4+...+1/N, где N – натуральное число.
# ===============================================================================================================
def calculate_series_sum(n: int) -> int:
    """
    Calculate the sum of the series 1 + 1/2 + 1/3 + ... + 1/N.

    Args:
        n (int): The value of N in the series.

    Returns:
        float: The sum of the series.

    """
    if n <= 0:
        return 0

    series_sum = 0
    for i in range(1, n + 1):
        series_sum += 1 / i

    return series_sum


try:
    n = int(input("Enter a natural number N: "))
    result = calculate_series_sum(n)
    print(f"The sum of the series 1 + 1/2 + 1/3 + ... + 1/{n} is: {result:.4f}")
except ValueError:
    print("Invalid input. Please enter a valid natural number.")
