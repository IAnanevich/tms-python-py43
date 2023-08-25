# Строки в Питоне сравниваются на основании значений символов.
# Т.е. если мы захотим выяснить, что больше: «Apple» или «Яблоко», – то «Яблоко» окажется большим.
# А все потому, что английская буква «A» имеет значение 65 (берется из таблицы кодировки),
# а русская буква «Я» – 1071 (с помощью функции ord() это можно выяснить).
# Такое положение дел не устроило Анну.
# Она считает, что строки нужно сравнивать по количеству входящих в них символов.
# Для этого девушка создала класс RealString и реализовала озвученный инструментарий.
# Сравнивать между собой можно как объекты класса, так и обычные строки с экземплярами класса RealString.
# К слову, Анне понадобилось только 3 метода внутри класса (включая __init__()) для воплощения задуманного.


class RealString:
    """Anna's class"""

    def __init__(self, word: str | object):
        self.word = str(word)

    # переопределим "=="
    def __eq__(self, other: str | object) -> bool:
        if not isinstance(other, RealString):
            other = RealString(other)
        return len(self.word) == len(other.word)

    # переопределим ">"
    def __gt__(self, other: str | object) -> bool:
        if not isinstance(other, RealString):
            other = RealString(other)
        return len(self.word) > len(other.word)


word_1 = RealString("Apple")
word_2 = RealString("Яблоко")
word_3 = "Melon"
word_4 = "555"

print(word_1 == word_2)  # False
print(word_1 == word_3)  # True
print(word_1 == word_4)  # False
print(word_1 > word_2)  # False
print(word_1 > word_3)  # False
print(word_1 > word_4)  # True
