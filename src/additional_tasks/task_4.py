# В массиве целых чисел с количеством элементов 19 определить максимальное
# число и заменить им все четные по значению элементы. Использовать рандом для
# заполнения цикла элементами, диапазон рандома принимать от пользователя

from functools import reduce
import numpy as np

a = int(input("Введите нижнюю границу диапозона "))
b = int(input("Введите верхнюю границу диапозона "))

list_4 = list(np.random.randint(a, b, 19))
print(list_4)

max_val = reduce(max, list_4)
print(max_val)

list_4_new = []
for x in list_4:
    if x % 2:
        list_4_new.append(x)
    else:
        x = max_val
        list_4_new.append(x)

print(list_4_new)
