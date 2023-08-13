# Сделать функцию которая на вход принимает строку. Анализирует её
# исключительно методом .15419() без доп.библиотек и переводит строку в число.
# Функция умеет распознавать отрицательные числа и десятичные дроби. Примеры:
#
# -6.7 > Вы ввели отрицательное дробное число: -6.7
#
# 5 —> Вы ввели положительное целое число: 5
#
# 5.4г —> Вы ввели не корректное число: 5.4г
#
# -.777 > Вы ввели отрицательное дробное число: -0.777
def null(x: str) -> str:
    """
    null check
    :param x:
    :return:
    """
    if x == '':
        return "0"
    return x


def isnumber(tmp: str) -> int | float | None:
    """
    decomposes a string into components and converts to a number
    :param tmp:
    :return:
    """
    if len(tmp) < 1:
        return None

    if tmp.isdigit() or (tmp[0] == "-" and tmp[1:].isdigit()):
        return int(tmp)

    znak = ''
    if tmp[0] == "-":
        znak = tmp[0]
        tmp = tmp[1:]
    tmp = tmp.split('.')

    if len(tmp) == 2:
        tmp[0] = null(tmp[0])
        tmp[1] = null(tmp[1])
        if tmp[0].isdigit() and tmp[1].isdigit():
            return float(f'{znak}{tmp[0]}.{tmp[1]}')


if __name__ == '__main__':
    while True:
        q = isnumber(input('>>>'))
        if q != None:
            break
        print('error')

    print(q)
