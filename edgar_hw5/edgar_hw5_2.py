# Дан список чисел. Посчитать сколько раз встречается каждое число. Использовать для подсчета функцию.
# Подсказка: для хранения данных использовать словарь. Для проверки нахождения элемента в словаре использовать метод
# GET(), либо оператор in. bg
# ------------------------------------------------------------------------------------------------------------------
from typing import List, Dict


def count_number(number_list: List[int]) -> Dict[int, int]:
    """
    Count the occurrences of each number in the list.
    :param number_list: List of integers
    :return: Dictionary where keys are numbers and values are their occurrences
    """
    count_dict = {}  # Create empty dictionary

    for num in number_list:
        count_dict[num] = count_dict.get(num, 0) + 1
    return count_dict


# Example list number
numbers = [1, 2, 3, 4, 1, 2, 4, 3, 5, 3, 6, 6, 3, 2, 1, 2, 3, 4, 5, 3, 1, 1, 1, 1, 1, 2]

# Counting the number of numbers using the function
result = count_number(numbers)

# Print result
for num, count in result.items():
    print(f'Numbers {num} occurs {count} times')
