# Строки в Питоне сравниваются на основании значений символов.
# Т.е. если мы захотим выяснить, что больше: «Apple» или «Яблоко», – то «Яблоко» окажется бОльшим.
# А все потому, что английская буква «A» имеет значение 65 (берется из таблицы кодировки),
# а русская буква «Я» – 1071 (с помощью функции ord() это можно выяснить).
# Такое положение дел не устроило Анну.
# Она считает, что строки нужно сравнивать по количеству входящих в них символов.
# Для этого девушка создала класс RealString и реализовала озвученный инструментарий.
# Сравнивать между собой можно как объекты класса, так и обычные строки с экземплярами класса RealString.
# К слову, Анне понадобилось только 3 метода внутри класса (включая __init__()) для воплощения задуманного.

class RealString:

    def __init__(self, value: str):
        self.value = value
        self.length = len(value)

    def __lt__(self, other: str | object) -> bool:
        if isinstance(other, RealString):
            return self.length < other.length
        elif isinstance(other, str):
            return self.length < len(other)
        else:
            return NotImplemented

    def __le__(self, other: str | object) -> bool:
        if isinstance(other, RealString):
            return self.length <= other.length
        elif isinstance(other, str):
            return self.length <= len(other)
        else:
            return NotImplemented


if __name__ == "__main__":
    apple = RealString("Apple")
    apple_ru = RealString("Яблоко")
    print(apple == apple_ru)
    print(apple != "trololo")
    print(apple < apple_ru)
    print("trololo" > apple_ru)
    print(apple >= apple_ru)
    print(apple <= "trololo")
