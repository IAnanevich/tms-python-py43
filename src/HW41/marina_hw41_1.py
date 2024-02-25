# В непустом массиве целых чисел nums, каждый элемент появляется дважды, кроме одного. Найдите его единственного.
# Сложность должна быть О(n)
# nums = [2,2,1] ответ: 1
# nums = [4,1,2,1,2] ответ: 4
# nums = [1] ответ: 1


def find_single_number(nums: list) -> int:
    """
    find single number in list of numbers
    :param nums: list of numbers
    :return: single number in list
    """
    result = 0
    for el in nums:
        result ^= el
    return result


# nums_1 = [1, 2, 2, 1, 6, 4, 5, 5, 4]
nums_1 = [4, 1, 2, 1, 2]
print(find_single_number(nums_1))
