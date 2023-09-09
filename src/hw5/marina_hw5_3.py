# Дан список чисел. Посчитать, сколько раз встречается каждое число. Использовать для подсчета функцию.
# Для хранения данных использовать словарь.
# Для проверки нахождения элемента в словаре использовать метод get(), либо оператор in.


def count_number(my_list: list[int]) -> dict[int, int]:
    count_dict = {}
    for i in range(len(my_list)):
        if count_dict.get(my_list[i]) is None:
            count_dict[my_list[i]] = my_list.count(my_list[i])
    return count_dict


example_list = [1, 2, 3, 1, 1, 5, 6, 5, 7, 2, 3, 5]
print(count_number(example_list))
