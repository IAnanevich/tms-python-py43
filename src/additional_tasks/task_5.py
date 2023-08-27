# Задан целочисленный массив. Определить количество участков массива, на
# котором элементы монотонно возрастают (каждое следующее число больше предыдущего).


def number_monotone_increase(number_list: list[int]) -> int:
    """
    find number of monotonically increasing intervals in original list
    :param number_list: original lisf for research
    :return: number of monotonically increasing intervals
    """
    count_interval = 0  # счетчик интервалов
    # дублируем последний элемент для проверки монотонности предыдущих
    number_list.append(number_list[-1])
    for i in range(1, len(number_list) - 1):
        # условие для точки, в которой прерывается монотонное возрастание
        if number_list[i - 1] < number_list[i] and number_list[i + 1] <= number_list[i]:
            count_interval += 1
    return count_interval


example_list = [1, 2, 3, 4, 2, 6, 3, 2, 7, 8, 2, 0, 4, 5]
print(f"Number of monotonic increase is {number_monotone_increase(example_list)}")
