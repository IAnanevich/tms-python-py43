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
    def __init__(self, str_1: str) -> None:
        """

        :param str_1: string
        """
        self.str_1 = str_1

    def __eq__(self, other) -> bool:
        """

        :param other: another object
        :return: true if length self = length another object
        """
        check = other if isinstance(other, str) else other.str_1
        return len(self.str_1) == len(check)

    def __gt__(self, other) -> bool:
        """

        :param other: another object
        :return: true if length self > length another object
        """
        check = other if isinstance(other, str) else other.str_1
        return len(self.str_1) > len(check)


one = RealString('Apple')
two = RealString('Яблоко')
three = 'mango'
print('1', one == two)
print('2', one > two)
print('3', one < two)
print('4', three == one)
print('5', one > three)
print('6', two > three)
print('7', two > 'hello')
