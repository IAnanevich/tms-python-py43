# Описать функцию fact2( n ), вычисляющую двойной факториал:n!! = 1·3·5·...·n,
# если n — нечетное; n!! = 2·4·6·...·n, если n — четное, n > 0 — параметр целого типа.
# С помощью этой функции найти двойные факториалы пяти данных целых чисел.


def double_fact(number: int) -> int:
    """
    make double factorial of the number
    :param number: base of double factorial
    :return: result of double factorial
    """
    if number < 3:
        return number
    return number * double_fact(number - 2)


numb_list = [5, 10, 3, 25, 4]

for i in numb_list:
    print(f"{i}!! is: {double_fact(i)}")
