# сделать свое исключени и подключить try/except
# треугольник существует тогда и только тогда, когда сумма двух его сторон больше третьей


class TriangleNotExist(Exception):
    def __init__(self, my_text: str) -> None:
        self.my_text = my_text
        super().__init__(self.my_text)


def sum_side(side_1: str, side_2: str, side_3: str) -> None:
    """

    :param side_1:
    :param side_2:
    :param side_3:
    :return:
    """
    if side_1.isnumeric() and side_2.isnumeric() and side_3.isnumeric():
        side_1 = float(side_1)
        side_2 = float(side_2)
        side_3 = float(side_3)
        if side_1 + side_2 > side_3 and side_2 + side_3 > side_1 and side_3 + side_1 > side_2:
            print("Треугольник существует")
        raise TriangleNotExist("Треугольник не существует")
    else:
        print("Введите число")


side_a = input("Введите сторону a: ")
side_b = input("Введите сторону b: ")
side_c = input("Введите сторону c: ")

try:
    sum_side(side_a, side_b, side_c)
except TriangleNotExist as error:
    print(error)
