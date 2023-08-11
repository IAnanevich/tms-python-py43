# Дан список чисел
# Посчитать сколько раз встречается каждое число
# Использовать функцию


def do_something(numbers: list) -> dict:
    """
     Посчитает сколько раз встречается каждое число в указанном списке и вернет таблицу вида [N : Q]
    :param numbers: any list of numbers
    :return: result of calculation number!
    """

    # Отобразим список
    print(f"\nThe list is {numbers}")

    # Получим множество уникальных числе
    set_of_numbers = set(numbers)

    # Запишем сколько раз число встречается в списке
    new_dict = {}
    for n in set_of_numbers:
        new_dict[n] = numbers.count(n)

    # Вернем результат
    return new_dict


list_of_numbers = [0, 2, 3, 4, 5, 6, 2, 2, 3, 4, 4, 5, 6, 5, 4, 3, 2, 0]
some_result = do_something(list_of_numbers)

# Отобразим шапку
print("\nN : Q")

# Отобразим таблицу
for e in some_result.items():
    print(f"{e[0]} : {e[1]}")
