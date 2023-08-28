# Для заданного числа N составьте программу вычисления суммы
# S=1+1/2+1/3+1/4+...+1/N, где N – натуральное число.

def harmonic_series(n: int) -> float:
    """ Return sum of the harmonic series.

    :param n: number of series
    :return: sum of the harmonic series
    """
    return sum(1/i for i in range(1, n + 1))


if __name__ == "__main__":
    number = input("Enter an integer: ")
    try:
        number = int(number)
    except TypeError as error:
        print(error)
    print(round(harmonic_series(number), 5))
