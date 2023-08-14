# написать лямбда-функцию, определяющую четное/нечетное число.

numbers = int(input('Введите число: '))

even_or_odd = lambda x: print('нечетное') if x % 2 else print('четное')

even_or_odd(numbers)
