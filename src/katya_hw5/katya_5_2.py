# Написать программу для нахождения факториала


def fact(a: int) -> int:
    """
    Calculating the factorial
    :param a: number a
    :return: number factorial
    """
    if a > 1:
        return a * fact(a-1)
    return 1


while True:
    number_fact = input('Введите число для подсчета факторияла: ')
    if number_fact.isdigit():
        number_fact_n = int(number_fact)
        if number_fact_n == 1:
            print('Факториал числа 1 равен 1')
        elif number_fact_n > 0:
            print(f'Факториял числа {number_fact_n} равен {fact(number_fact_n)}')
        else:
            print('Введите число больше О')
    else:
        print('Введите число')