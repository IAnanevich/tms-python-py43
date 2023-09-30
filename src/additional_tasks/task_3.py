# Для заданного числа N составьте программу вычисления суммы
# S=1+1/2+1/3+1/4+...+1/N, где N – натуральное число.


def do_sum_of_series(numb: int) -> float:
    """
    calculates the sum of a series
    :param numb: number of term
    :return: sum of series
    """
    if numb == 1:
        return 1 / numb
    return 1 / numb + do_sum_of_series(numb - 1)


while True:
    n = input("Enter integer number(> 0): ")
    # сумма ряда может быть посчитана только для натуральных чисел, больших нуля
    if n.isdigit() and int(n):
        print(f"Sum of series is: {do_sum_of_series(int(n))}")
        break
    print("You need to enter an INTEGER number. Try again")
