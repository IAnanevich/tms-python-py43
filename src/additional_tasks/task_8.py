# Для каждого натурального числа в промежутке от m до n
# Вывести все делители кроме единицы и самого числа
# Где m и n вводятся с клавиатуры

def all_deviders(number: int) -> list:
    """
    Ищет все делители натурального числа
    :param number: Натуральное число
    :return: Вернет все делители списком
    """
    devs = list()
    for dev in range(2, number):  # кроме единицы и самого числа
        if not number % dev:
            devs.append(dev)
    return devs


# m вводbтся с клавиатуры
some_input_m = input("Натуральное число M: >>")
try:
    m = int(some_input_m)
    m = max(m, -m, 1)
except ValueError:
    print("Получится в следующий раз... m = 10")
    m = 10

# n вводbтся с клавиатуры
some_input_n = input("Натуральное число N: >>")
try:
    n = int(some_input_n)
    n = max(n, -n, 1)
except ValueError:
    print("Получится в следующий раз... N = 100")
    n = 100

# Для каждого натурального числа в промежутке от m до n вывести все делители
for x in range(m, n + 1):
    all_devs = all_deviders(x)
    if all_devs:
        print(f"Делители числа {x} это: ", all_devs)
