def number_list(numbers_list: list) -> dict:
    """
    :param numbers_list: A list of numbers
    :return: Dictionary
    """
    lister = {}
    for num in numbers_list:
        if lister.get(num) is not None:
            lister[num] += 1
        else:
            lister[num] = 1
    return lister


numbers = [5, 5, 5, 5, 5, 1, 1, 1, 12, 2, 2]
result = number_list(numbers)
for number, count in result.items():
    print(f"Число {number} встречается {count} раз")
