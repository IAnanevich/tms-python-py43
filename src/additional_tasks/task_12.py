# Создать декоратор для функции, которая принимает список чисел.
# Декоратор должен производить предварительную проверку данных:
# удалять все четные элементы из списка.
import random


def exclude_even(func) -> None:
    """
    # Декоратор должен производить предварительную проверку данных:
    # удалять все четные элементы из списка.
    :param numbers:  список чисел
    :return: производит предварительную проверку
    """
    def inner_check(numbers: list) -> None:
        """
        :param numbers: список чисел
        :return: производит предварительную проверку
        """
        for number in numbers:
            if not number % 2:
                numbers.remove(number)
                inner_check(numbers)

        return func(numbers)

    return inner_check


@exclude_even
def some_function(numbers: list) -> None:
    """
    Заглушка
    :param numbers: список чисел
    :return: None
    """
    len(numbers)


# В массиве целых чисел с количеством элементов 22
some_list = list()
for i in range(1, 23):
    some_list.append(random.randint(1, 100))

print("\nBefore: ", some_list)
some_function(some_list)
print("After: ", some_list)
