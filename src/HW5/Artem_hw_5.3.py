# Дан список чисел. Посчитать, сколько раз встречается каждое число. Использовать для подсчета функцию.
# Для хранения данных использовать словарь.
# Для проверки нахождения элемента в словаре использовать метод get(), либо оператор in.
def count(dict_1):
    """

    :param dict_1: dictionary with numbers
    :return: dictionary the number of each number in the list
    """
    new_dict = {}
    for i in dict_1:
        new_dict[i] = new_dict.get(i, 0) + 1
    return new_dict


dict_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 9, 8]
print(count(dict_1))
