# Дан список чисел. Посчитать сколько раз встречается каждое числою


def check_number(elements: list[int | str]) -> dict[int | str]:
    """
    Counting the number of identical sequence elements
    :param elements: list
    :return: dict
    """
    check = {}
    for i in elements:
        check[i] = check.get(i, 0) + 1
    return check


list_5_3 = [1, 7, 8, 9, 5, 'hello', 7, 3, 7, 7, 7, 'hello']

result = check_number(list_5_3)
print(result)
