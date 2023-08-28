# Два натуральных числа называют дружественными, если каждое из них равно
# сумме всех делителей другого, кроме самого этого числа. Найти все пары
# дружественных чисел, лежащих в диапазоне от 200 до 300.
# ================================================================================================================
from typing import List, Tuple


def sum_of_divisors(n: int) -> int:
    """
    Calculate the sum of proper divisors of a given number.
    :param n: The number for which to calculate the sum of divisors.
    :return: The sum of proper divisors of the given number.
    """
    divisors_sum = 0
    for i in range(1, n // 2 + 1):
        if n % i == 0:
            divisors_sum += i
    return divisors_sum


def find_friendly_numbers(start: int, end: int) -> List[Tuple[int, int]]:
    """
    Find pairs of friendly numbers in a given range.
    :param start: The start of the range.
    :param end: The end of the range.
    :return: A list of tuples containing pairs of friendly numbers.
    """
    friendly_pairs = []
    for num1 in range(start, end + 1):
        sum1 = sum_of_divisors(num1)
        if start <= sum1 <= end:
            sum2 = sum_of_divisors(sum1)
            if num1 == sum2 and num1 != sum1:
                friendly_pairs.append((num1, sum1))
    return friendly_pairs


start_range = 200
end_range = 300
friendly_pairs = find_friendly_numbers(start_range, end_range)

print("Friendly number pairs:")
for pair in friendly_pairs:
    print(pair)
