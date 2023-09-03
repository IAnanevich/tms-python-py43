"""
1) Строки в Питоне сравниваются на основании значений символов.
Т.е. если мы захотим выяснить, что больше: «Apple» или «Яблоко», – то «Яблоко»
окажется бОльшим.
А все потому, что английская буква «A» имеет значение 65 (берется из таблицы кодировки),
а русская буква «Я» – 1071 (с помощью функции ord() это можно выяснить).
Такое положение дел не устроило Анну.
Она считает, что строки нужно сравнивать по количеству входящих в них символов.
Для этого девушка создала класс RealString и реализовала озвученный инструментарий.
Сравнивать между собой можно как объекты класса, так и обычные строки с экземплярами
класса RealString.
К слову, Анне понадобилось только 3 метода внутри класса (включая __init__())
для воплощения задуманного.
"""


class RealString:
    def __init__(self, row: str):
        self.row = row
        self.len_row = len(row)

    def __eq__(self, other: str | object) -> bool:
        """ Определяет поведение оператора равенства, == """
        if not isinstance(other, RealString):
            other = RealString(other)
        return self.len_row == other.len_row

    def __ne__(self, other: str | object) -> bool:
        """ Определяет поведение оператора неравенства, != """
        if not isinstance(other, RealString):
            other = RealString(other)
        return self.len_row != other.len_row

    def __lt__(self, other: str | object) -> bool:
        """ Определяет поведение оператора меньше, < """
        if not isinstance(other, RealString):
            other = RealString(other)
        return self.len_row < other.len_row

    def __gt__(self, other: str | object) -> bool:
        """ Определяет поведение оператора больше, > """
        if not isinstance(other, RealString):
            other = RealString(other)
        return self.len_row > other.len_row

    def __le__(self, other: str | object) -> bool:
        """ Определяет поведение оператора меньше или равно, <= """
        if not isinstance(other, RealString):
            other = RealString(other)
        return self.len_row <= other.len_row

    def __ge__(self, other: str | object) -> bool:
        """ Определяет поведение оператора больше или равно, >= """
        if not isinstance(other, RealString):
            other = RealString(other)
        return self.len_row >= other.len_row


if __name__ == "__main__":
    str_1 = RealString("Яблоко")
    str_2 = RealString("Apple")

    print("Яблоко" > str_2)
    print(str_1 > "Apple")
    print(str_1 < str_2)
    print(str_1 > str_2)

    print(str_1 <= str_2)
    print(str_1 >= str_2)

    print("Яблоко" == str_1)
    print("Яблоко" == str_2)
    print("Яблоко" != str_1)
    print("Яблоко" != str_2)
    print(str_1 == str_2)
    print(str_1 != str_2)
