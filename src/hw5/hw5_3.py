# Дан список чисел
# Посчитать сколько раз встречается каждое число
# Использовать функцию


def do_cal(numbers: list) -> None:
    """
    :param numbers: any list of numbers
    """

    # Отобразим список
    print(f"\nThe list is {numbers}")
    # Отобразим шапку
    print("N : Q")

    # Получим множество уникальных числе
    set_of_numbers = set(numbers)

    # Отобразим сколько раз число встречается в списке
    for n in set_of_numbers:
        print(f"{n} : {numbers.count(n)}")


list_of_numbers = [0, 2, 3, 4, 5, 6, 2, 2, 3, 4, 4, 5, 6, 5, 4, 3, 2, 0]
do_cal(list_of_numbers)
