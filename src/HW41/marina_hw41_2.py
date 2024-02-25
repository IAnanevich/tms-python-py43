# Напишите алгоритм, определяющий, является ли число n счастливым.
# Счастливое число — это число, определяемое следующим процессом:
# Начиная с любого положительного целого числа, замените число суммой квадратов его цифр.
# Повторяйте процесс до тех пор, пока число не станет равным 1 (где оно и останется),
# или пока он не будет повторяться бесконечно в цикле, который не включает 1.
# Счастливыми являются те числа, для которых этот процесс заканчивается на 1.
# Верните true, если n — счастливое число, и false, если нет.
# Пример 1: n = 19 ответ: true
# Пример 2: n = 2 ответ: false

from functools import reduce


def number_square(res: int, x: int) -> int:
    """
    returned summ of first number and square of second
    :param res: start number
    :param x: value for squaring
    :return: result of summ
    """
    res += x**2
    return res


def is_lucky_number(numb: int) -> bool:
    """
    checked id number is lucky
    :param numb: number for checking
    :return: is lucky number (True or False)
    """
    # список полученных сумм квадратов цифр числа
    list_square = []
    while True:
        # делим число на цифры
        list_num = list(map(int, str(numb)))
        # находим сумму квадратов цифр числа
        summ_of_squares = reduce(number_square, list_num, 0)
        # или = reduce(lambda x, y: x + y ** 2, list_num, 0)
        if summ_of_squares == 1:  # счастливое число
            return True
        elif summ_of_squares in list_square:  # цикл - несчастливое число
            return False
        else:
            # обновляем список полученных чисел - сумм квадратов
            list_square.append(summ_of_squares)
            # проверяем следующее число
            numb = summ_of_squares


while True:
    n = input("Please, enter positive integer number: ")
    try:
        int(n)
    except ValueError:
        print("Try again, your number is wrong")
        continue
    if int(n) > 0:
        print(f"Is number {n} lucky? {is_lucky_number(int(n))}")
        break
    else:
        print("You should enter POSITIVE integer number, try again.")
