# Написать программу для нахождения факториала


def fact(a: int) -> int:
    """
    Calculating the factorial
    :param a: number a
    :return: number factorial
    """
    if a > 1:
        return a * fact(a-1)
    else:
        return 1


number_fact = int(input('ВВедите число для подсчета факторияла'))

if number_fact == 1:
    print('Факториал числа 1 равен 1')
elif number_fact >0:
    print(f'Факториял числа {number_fact} равен {fact(number_fact)}')
else:
    print('Введите число больше О')
