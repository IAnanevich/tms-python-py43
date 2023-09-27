# дан список чисел, посчитать сколько раз встречается каждое число использу функцию
def quantity_in(list_x) -> dict:
    """
    finds the number of occurrences
    :param list_x: list of numbers
    :return:
    """
    return {i: list_x.count(i) for i in set(list_x)}


print(quantity_in([1, 3, 2, 3, 4, 3, 9, 5, 3, 9]))
