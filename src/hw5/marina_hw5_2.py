# Написать программу для нахождения факториала.
# Выполнить в виде рекурсивной функции


def do_factorial(numb: int) -> int:
    if numb == 1:
        return numb
    else:
        return numb * do_factorial(numb - 1)


number = int(input('Enter number to do factorial of it: '))
print(f'{number}! is {do_factorial(number)}')
