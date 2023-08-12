# Написать лямбда-функцию, определяющую четное/нечетное.
# Функция принимает параметр(число) и выдает слово "четное", если нет - "нечетное"

even_or_odd = lambda x: 'odd' if x % 2 else 'even'

while True:
    n = input('Enter integer number: ')
    if n.isdigit():
        print(f'Your number is {even_or_odd(int(n))}')
        break
    print('You need to enter integer number, try again')
