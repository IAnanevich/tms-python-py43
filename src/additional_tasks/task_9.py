# Описать функцию fact2( n ), вычисляющую двойной факториал :n!! = 1·3·5·...·n,
# если n — нечетное; n!! = 2·4·6·...·n, если n — четное (n > 0 — параметр целого типа.
# С помощью этой функции найти двойные факториалы пяти данных целых чисел.

def fact2(x: int) -> int:
    """ Find x!!.

        :param x: double factorial of this number
        :return: double factorial of x
        """
    return x * fact2(x - 2) if x > 0 else 1


if __name__ == "__main__":
    number = input("Enter a non-negative integer: ")
    try:
        number = int(number)
        if number < 0:
            raise ValueError
    except TypeError as error:
        print(error)
    print(fact2(number))
