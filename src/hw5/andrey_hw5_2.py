# Написать программу для нахождения факториала число
def factorial(n: int) -> int:
    """
    factorial of a number
    :type n: object
    """
    if n == 1:
        return 1
    return n * factorial(n - 1)


if __name__ == '__main__':
    try:
        n = int(input('Enter n: '))
        print(f'factorial {n} = {factorial(n)}')
    except ValueError:
        print('entered not an integer')
