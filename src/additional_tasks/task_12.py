# Создать декоратор для функции, которая принимает список чисел.
# Декоратор должен производить предварительную проверку данных:
# удалять все четные элементы из списка.
import random


def exclude_even(func) -> callable:
    """
    Декоратор должен производить предварительную проверку данных: удалять все четные элементы из списка.
    :param func: Функция для проверки
    :return: ничего
    """
    def wrapper(*args) -> None:
        """
        Обертка для вызова проверки и самой функции
        :param args:  набор параметров родителя
        :return: ничего
        """
        def inner_check(*params) -> None:
            """
            Удаляет все четные элементы из списка
            :param params: набор параметров родителя
            :return: ничего
            """
            numbers = params[0]
            for number in numbers:
                if not number % 2:
                    numbers.remove(number)
                    inner_check(numbers)

        inner_check(*args)
        return func(*args)
    return wrapper


@exclude_even
def some_function(numbers: list) -> None:
    """
    Заглушка
    :param numbers: список чисел
    :return: None
    """
    print("After: ", numbers)


# В массиве целых чисел с количеством элементов 22
some_list = list()
for i in range(1, 23):
    some_list.append(random.randint(1, 100))

print("\nBefore: ", some_list)
some_function(some_list)
