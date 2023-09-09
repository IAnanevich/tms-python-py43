# Написать программу для нахождения факториала.
# Выполнить в виде рекурсивной функции


def do_factorial(numb: int) -> int:
    if numb == 1:
        return numb
    return numb * do_factorial(numb - 1)


while True:
    number = input('Enter number to do factorial of it: ')
    if number.isdigit():
        number = int(number)
        print(f'{number}! is {do_factorial(number)}')
        break
    print('You need to enter integer-number to do factorial of it, try again)')
