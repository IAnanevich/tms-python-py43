# Описать функцию fact2( n ), вычисляющую двойной факториал :
# n!! = 1·3·5·...·n, если n — нечетное; n!! = 2·4·6·...·n,
# если n — четное (n > 0 — параметр целого типа.
# С помощью этой функции найти двойные факториалы пяти данных целых чисел


def fact2(a: int) -> int:
    """
    Calculating the factorial
    :param a: number a
    :return: number factorial
    """
    if a > 1:
        return a * fact2(a - 2)
    return 1


while True:
    number_fact = input("Введите число для подсчета двойного факторияла: ")
    if number_fact.isdigit():
        number_fact_n = int(number_fact)
        if number_fact_n == 1:
            print("Факториал числа 1 равен 1")
        elif number_fact_n > 0:
            print(f"Двойной факториял числа {number_fact_n} равен {fact2(number_fact_n)}")
        else:
            print("Введите число больше О")
    else:
        print("Введите число")
