# написать лямбда-функцию, определяющую четное/нечетное число.

numbers = int(input('Введите число: '))

even_or_odd = lambda x: print('четное') if x % 2 == 0 else print('нечетное')

even_or_odd(numbers)
