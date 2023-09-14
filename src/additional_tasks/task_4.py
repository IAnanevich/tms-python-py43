# В массиве целых чисел с количеством элементов 19
# определить максимальное число и заменить им все четные по значению элементы.
# Использовать рандом для заполнения цикла элементами, диапазон рандома принимать от пользователя
import random

# Диапазон рандома принимать от пользователя
some_input = input("\nНатуральное число как диапазон рандома >>")
try:
    max_random = int(some_input)
    max_random = max(max_random, -max_random, 1)
except ValueError:
    print("Получится в следующий раз... 100")
    max_random = 100

# В массиве целых чисел с количеством элементов 19
some_list = list()
for i in range(1, 20):
    some_list.append(random.randint(1, max_random))

# Определить максимальное число
max_number = 0
for number in some_list:
    max_number = max(max_number, number)

# Промежуточные значения
print("Count:", len(some_list))
print("Max number is", max_number)
print("Before", some_list)

# Заменить им все четные по значению элементы
for i in range(len(some_list)):
    if not some_list[i] % 2:
        some_list[i] = max_number

# Конечные значения
print("After", some_list)
