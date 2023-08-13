# Написать программу для нахождения факториала число
def factorial(n: int) -> int:
    """
    factorial of a number
    :type n: object
    """
    if n == 0:
        return 1
    return n * factorial(n - 1)


if __name__ == '__main__':
    n = input('Enter n: ')
    try:
        n = int(n)
    except ValueError as error:
        n = 0
        print(f'{error}, entered not an integer')
    print(f'factorial {n} = {factorial(n)}')
