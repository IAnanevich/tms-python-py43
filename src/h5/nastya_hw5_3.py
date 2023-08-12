"""Дан список чисел. Посчитать сколько раз встречается каждое число.
Использовать для подсчёта функцию.
Подсказка: для хранения данных использовать словарь.
Для проверки нахождения элемента в словаре использовать метод get(), либо оператор in. """


def cou(k: list | tuple | set) -> dict:
    """
    Counts what number and how many times it is repeated
    :param k: list
    :return: dict with key: what number, value: how many times it is repeated
    """
    new_dict = {}
    for i in k:
        new_dict[i] = new_dict.get(i, 0) + 1
    return new_dict


j = [1, 2, 3, 4, 5, 5, 5]
print(cou(j))
