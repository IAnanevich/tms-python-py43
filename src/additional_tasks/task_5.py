# Задан целочисленный массив.
# Определить количество участков массива, на котором элементы монотонно возрастают
# (каждое следующее число больше предыдущего)
import random

# Задан целочисленный массив.
some_list = list()
for i in range(0, 22):
    some_list.append(random.randint(1, 100))

# Промежуточные значения
print("\nCount:", len(some_list))
print("Before", some_list)

# Определить количество участков массива, на котором элементы монотонно возрастают
counts = 0
last_number = None
is_grow = False
for number in some_list:

    # Первый элемент массива
    if not isinstance(last_number, int):
        last_number = number
        continue

    # Каждый следующий элемент массива
    if number > last_number:
        last_number = number
        if not is_grow:
            counts += 1  # возрастают
        is_grow = True
        continue

    last_number = number
    is_grow = False

# Конечные значения
print("Количество участков массива, на котором элементы монотонно возрастают = ", counts)
