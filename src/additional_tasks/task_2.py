# Два натуральных числа называют дружественными, если каждое из них равно
# сумме всех делителей другого, кроме самого этого числа.
# Найти все пары дружественных чисел, лежащих в диапазоне от 200 до 300


def sum_of_divisors(numb: int) -> int:
    """
    find sum of divisors a number without this number
    :param numb: integer number from interval
    :return: sum of divisors
    """
    return sum([j for j in range(1, numb // 2 + 1) if not numb % j])


a = 200  # левая граница интервала
b = 300  # правая граница интервала
for i in range(a, b + 1):
    friend_numb = sum_of_divisors(i)
    # проверка на совпадение чисел с суммой делителей и добавляем условие, что второе число д/б больше исходного,
    # чтобы не дублировать пары просто в другой последовательности
    if i < friend_numb <= b and i == sum_of_divisors(friend_numb):
        print(f"{i} and {friend_numb}")
