# Создать декоратор для функции, которая принимает список чисел.
# Декоратор должен производить предварительную проверку данных - удалять все четные элементы из списка.

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]


def decor(func):
    def delite_even_numbers(*args):
        for i in args:
            return func([i for i in args[-1] if i % 2 != 0])

    return delite_even_numbers


@decor
def print_func(value):
    return value


print(print_func(my_list))
