# Написать программу для нахождения факториала.
def fact(n):
    """

    :param n: defined as the product of all natural numbers from 1 to n inclusive
    :return: factorial
    """
    if n == 1:
        return 1
    return n * fact(n - 1)


number = input('Enter number: ')
if number.isdigit():
    number = int(number)
    print(f'factorial of a number: {fact(number)}')
else:
    print('Enter a number')
