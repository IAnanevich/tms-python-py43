# '''Решить квадратное уравнение вида ax^2+bx+c=0
# Коэффициенты a,b,c вводятся с клавиатуры .
# Рассмотреть все случаи дискриминанта.'''
#
# import math
# a = float(input("Введите коэффициент a: "))
# b = float(input("Введите коэффициент b: "))
# c = float(input("Введите коэффициент c: "))
# discriminant = b**2 - 4*a*c
# if discriminant > 0:
#     x1 = (-b + math.sqrt(discriminant)) / (2*a)
#     x2 = (-b - math.sqrt(discriminant)) / (2*a)
#     print("Уравнение имеет два корня:")
#     print("x1 =", x1)
#     print("x2 =", x2)
# elif discriminant == 0:
#     x = -b / (2*a)
#     print("Уравнение имеет один корень:")
#     print("x =", x)
# else:
#     print("Нет корней")

# '''Дан список целых чисел.Создать новый список,
# каждый элемент которого равен исходному элементу умноженному на -2.'''
#
# result = [-2 * i for i in [1, 3, 5, 6, 2]]
# print(result)

# '''Дан список целых чисел.
# Подсчитать сколько четных чисел в списке.'''
#
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,12,14,16]
# counter = 0
# for num in numbers:
#     if num % 2 == 0:
#         counter += 1
# print(f'Количество четных чисел в списке: {counter}')

# '''Дан словарь: {'test': 'test_value', 'europe': 'eur', 'dollar': 'usd', 'ruble': 'rub'}
# Добавить каждому ключу число равное длине этого ключа (пример {‘key’: ‘value’} -> {‘key3’:‘value’}).
# Чтобы получить список ключей - использовать метод .keys()'''
#
# dictionary = {'test': 'test_value', 'europe': 'eur', 'dollar': 'usd', 'ruble': 'rub'}
# new_dictionary = {}
# for key in dictionary.keys():
#     new_key = key + str(len(key))
#     new_dictionary[new_key] = dictionary[key]
# print(new_dictionary)

# '''Дан список. Создать новый список,
# сдвинутый на 1 элемент влево. Пример: 1 2 3 4 5 -> 2 3 4 5 1'''
#
# list_1=[1,3,5,7,9]
# print(list_1[1:]+list_1[:1])

# '''Составить список чисел Фибоначчи содержащий 15 элементов.
# (Подсказка: Числа Фибоначчи - последовательность, в которой первые два числа равны либо 1 и 1,
# а каждое последующее число равно сумме двух предыдущих чисел. Пример: 1, 1, 2, 3, 5, 8, 13, 21, 34... )'''
#
# n = 15
# fibonacci = [0, 1]
# while len(fibonacci) < n:
#     next_number = fibonacci[-1] + fibonacci[-2]
#     fibonacci.append(next_number)
# print(fibonacci)