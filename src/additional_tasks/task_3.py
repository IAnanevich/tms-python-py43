# Для заданного числа N составьте программу вычисления суммы
# S=1+1/2+1/3+1/4+...+1/N, где N – натуральное число.
def sum_n(a: int) -> int:
    """
    Calculating the factorial
    :param a: number a
    :return: number factorial
    """
    if a > 1:
        return 1 / a + sum_n(1 / (a - 1))
    return 1


while True:
    number_sum = input("Введите число для суммы: ")
    if number_sum.isdigit():
        number_sum_n = int(number_sum)
        if number_sum_n == 1:
            print("сумма равен 1")
        elif number_sum_n > 0:
            print(f"сумма чисел 1/{number_sum_n} до 1 равна {sum_n(number_sum_n)}")
        else:
            print("Введите число больше О")
    else:
        print("Введите число")
