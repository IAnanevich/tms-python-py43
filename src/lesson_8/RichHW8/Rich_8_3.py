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
    def __init__(self, string):
        """
        :param string: =
        """
        self.string = string

    def __lt__(self, other):
        """
        :param other: < (less)
        :return:
        """
        return len(self.string) < len(other.string)

    def __le__(self, other):
        """
        :param other: (less or equal)
        :return:
        """
        return len(self.string) <= len(other.string)

    def __eq__(self, other):
        """
        :param other: == (comparison)
        :return:
        """
        return len(self.string) == len(other.string)

    def __ne__(self, other):
        """
        :param other: != equality
        :return:
        """
        return len(self.string) != len(other.string)

    def __gt__(self, other):
        """
        :param other: > more
        :return:
        """
        return len(self.string) > len(other.string)

    def __ge__(self, other):
        """
        :param other: >= (more equal)
        :return:
        """
        return len(self.string) >= len(other.string)


# Create class instances
string1 = RealString("Яблоко")
string2 = RealString("Apple")


# Compare class objects with each other
print(string1 < string2)
print(string1 <= string2)
print(string1 == string2)
print(string1 != string2)
print(string1 > string2)
print(string1 >= string2)
