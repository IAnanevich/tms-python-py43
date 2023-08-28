# Задан целочисленный массив. Определить количество участков массива, на
# котором элементы монотонно возрастают (каждое следующее число больше
# предыдущего).
# ===============================================================================================================

from typing import List


def count_increasing_sections(arr: List[int]) -> int:
    """
    Count the number of increasing sections in the integer array.

    Args:
        arr (List[int]): The list of integers.

    Returns:
        int: The number of increasing sections.
    """
    count = 0
    increasing = False

    for i in range(1, len(arr)):
        if arr[i] > arr[i - 1]:
            if not increasing:
                increasing = True
                count += 1
        else:
            increasing = False

    return count


try:
    input_str = input("Enter the integer array (comma-separated): ")
    array = [int(x) for x in input_str.split(",")]

    sections = count_increasing_sections(array)
    print(f"Number of increasing sections: {sections}")
except ValueError:
    print("Invalid input. Please enter a valid comma-separated list of integers.")
