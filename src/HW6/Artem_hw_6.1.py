# написать лямбда-функцию оределеяющую четное\нечетное

number_one = lambda a: print('even') if a % 2 == 0 else print('uneven')

a = input()
if a.isdigit():
    print('Your number is: ', end=''), number_one(int(a))
else:
    print("Enter a number")
