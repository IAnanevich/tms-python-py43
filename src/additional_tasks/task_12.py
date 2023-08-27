# Создать декоратор для функции, которая принимает список чисел.
# Декоратор должен производить предварительную проверку данных - удалять все четные элементы из списка.


def del_even_numbers(func):
    def inner(args):
        return func([i for i in args if i % 2])

    return inner


@del_even_numbers
def print_number_list(my_list: list[int]) -> None:
    """
    print array
    :param my_list: original list of numbers
    :return: nothing
    """
    print(*my_list)


list_num = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print_number_list(list_num)
