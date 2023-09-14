# В массиве целых чисел с количеством элементов 19 определить максимальное
# число и заменить им все четные по значению элементы. Использовать рандом для
# заполнения цикла элементами, диапазон рандома принимать от пользователя.
# ==================================================================================================================

import random
from typing import List


def replace_even_with_max(arr: List[int]) -> None:
    """
    Replace even elements in the list with the maximum value in the list.

    Args:
        arr (List[int]): The list of integers.

    Returns:
        None
    """
    max_num = max(arr)
    for i in range(len(arr)):
        if arr[i] % 2 == 0:
            arr[i] = max_num


try:
    lower_range = int(input("Enter the lower range of random numbers: "))
    upper_range = int(input("Enter the upper range of random numbers: "))

    if lower_range >= upper_range:
        print("Invalid range. The lower range should be less than the upper range.")
    else:
        array = [random.randint(lower_range, upper_range) for _ in range(19)]
        print("Original array:", array)

        replace_even_with_max(array)
        print("Array after replacing even numbers with max:", array)
except ValueError:
    print("Invalid input. Please enter valid range values.")
