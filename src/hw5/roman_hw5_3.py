'''Дан список чисел. Посчитать сколько раз встречается каждое число.
Использовать для подсчёта функцию. Подсказка: для хранения данных
использовать словарь. Для проверки нахождения элемента в словаре
использовать метод get() , либо оператор in'''


def count_numbers(numbers):
    counts = {}
    for num in numbers:
        counts[num] = counts.get(num, 0) + 1
    return counts


numbers = [5, 8, 2, 4, 8, 8, 5, 2, 4, 5, 1, 5]
result = count_numbers(numbers)
print(result)
