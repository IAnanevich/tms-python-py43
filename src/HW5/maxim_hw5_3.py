# Дан список чисел. Посчитать сколько раз встречается каждое число.
# Использовать для подсчёта функцию.
# Подсказка: для хранения данных использовать словарь. Для проверки нахождения
# элемента в словаре использовать метод get(), либо оператор in.

def repetitions(ls: list) -> dict:
    """
    Return dict where the keys are the list items and the value is the number of their repetitions

    :param ls: list for processing
    :return: dict where the keys are the list items and the value is the number of their repetitions
    """
    _dict = dict()
    for i in ls:
        _dict[i] = _dict.get(i, 0) + 1
    return _dict


if __name__ == '__main__':
    print(repetitions([1, 2, 3, 4, 5, 5, 6, 7, 3, 4, 5]))
