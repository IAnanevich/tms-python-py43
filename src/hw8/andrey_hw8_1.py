# Строки в Питоне сравниваются на основании значений символов.
# Т.е. если мы захотим выяснить, что больше: «Apple» или «Яблоко», – то «Яблоко» окажется бОльшим.
# А все потому, что английская буква «A» имеет значение 65 (берется из таблицы кодировки),
# а русская буква «Я» – 1071 (с помощью функции ord() это можно выяснить).
# Такое положение дел не устроило Анну.
# Она считает, что строки нужно сравнивать по количеству входящих в них символов.
# Для этого девушка создала класс RealString и реализовала озвученный инструментарий.
# Сравнивать между собой можно как объекты класса, так и обычные строки с экземплярами класса RealString.
# К слову, Анне понадобилось только 3 метода внутри класса (включая __init__()) для воплощения задуманного

class RealString:
    def __init__(self, row: str | object):
        try:
            self.row = str(row)
        except ValueError as e:
            print(e)

    def __lt__(self, other: str | object) -> bool:
        if not isinstance(other, RealString):
            other_new = RealString(other)
        else:
            other_new = other
        return len(self.row) < len(other_new.row)

    def __le__(self, other: str | object) -> bool:
        if not isinstance(other, RealString):
            other_new = RealString(other)
        else:
            other_new = other
        return len(self.row) <= len(other_new.row)


if __name__ == "__main__":
    apple = RealString("Apple")
    apple_ru = RealString("Яблоко")
    print(apple == apple_ru)
    print(apple != "trololo")
    print(apple < apple_ru)
    print(apple > apple_ru)
    print("trololo" > apple_ru)
    print(apple >= apple_ru)
    print(apple <= "trololo")
