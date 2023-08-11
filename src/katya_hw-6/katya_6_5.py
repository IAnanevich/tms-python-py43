# написать лямбда-функцию, определяющую четное/нечетное число.

numbers = int(input(f'Введите число: '))

even_or_odd = lambda x: print(f'четное') if x/2 == 0 else print(f'нечетное')

print(even_or_odd(numbers))
