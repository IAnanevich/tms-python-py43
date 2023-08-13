#написать лямбда-функцию оределеяющую четное\нечетное

a = int(input('Enter your number'))
x = 'even'
b = 'uneven'

number_one = lambda x, b: x if a % 2 == 0 else b
print(number_one(x,b))


