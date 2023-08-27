# В массиве целых чисел с количеством элементов 19 определить максимальное число
# и заменить им все четные по значению элементы.
# Использовать рандом для заполнения цикла элементами, диапазон случайных чисел принимать от пользователя.

from random import randint


def change_list(list_number: list[int]) -> list[int]:
    """
    change original list of integer numbers
    :param list_number: original list of integer number
    :return: changed list integer numbers
    """
    max_number_list = max(list_number)
    return [max_number_list if not i % 2 else i for i in list_number]


len_list = 19  # количество элементов списка
list_number_rand = []

while True:
    m = input("Enter integer number start of interval for elements: ")
    n = input("Enter integer number end of interval for elements: ")
    if m.isdigit() and n.isdigit():
        m, n = int(m), int(n)
        for _ in range(len_list):
            list_number_rand.append(randint(m, n))
        break
    print("You need to enter two INTEGER number. Try again")
# выводим исходный и преобразованный списки
print(f"Original list of numbers is:\n{list_number_rand}")
print(f"Changed list of numbers is:\n{change_list(list_number_rand)}")
