# Строки в Питоне сравниваются на основании значений символов.
# Т.е. если мы захотим выяснить, что больше: «Apple» или «Яблоко», – то «Яблоко» окажется бОльшим.
# А все потому, что английская буква «A» имеет значение 65 (берется из таблицы кодировки),
# а русская буква «Я» – 1071 (с помощью функции ord() это можно выяснить).
# Такое положение дел не устроило Анну.
# Она считает, что строки нужно сравнивать по количеству входящих в них символов.
# Для этого девушка создала класс RealString и реализовала озвученный инструментарий.
# Сравнивать между собой можно как объекты класса, так и обычные строки с экземплярами класса RealString.
# К слову, Анне понадобилось только 3 метода внутри класса (включая __init__()) для воплощения задуманного.
# ============================================================================================================

class RealString:
    def __init__(self, value: str):
        """
        Initialize a RealString object.
        :param value: The string value.
        """
        self.value = value

    def compare(self, other: 'RealString') -> int:
        """
        Compare the length of two RealString objects.
        :param other: Another RealString object.
        :return: -1 if self is shorter, 0 if lengths are equal, 1 if self is longer.
        """
        if len(self.value) < len(other.value):
            return -1
        elif len(self.value) == len(other.value):
            return 0
        else:
            return 1

    def __lt__(self, other: 'RealString') -> bool:
        """
        Implement the '<' operator for RealString objects.
        :param other: Another RealString object.
        :return: True if self is shorter than other, False otherwise.
        """
        return self.compare(other) == -1

    def __eq__(self, other: 'RealString') -> bool:
        """
        Implement the '==' operator for RealString objects.
        :param other: Another RealString object.
        :return: True if self and other have equal lengths, False otherwise.
        """
        return self.compare(other) == 0

    def __gt__(self, other: 'RealString') -> bool:
        """
        Implement the '>' operator for RealString objects.
        :param other:Another RealString object.
        :return: True if self is longer than other, False otherwise.
        """
        return self.compare(other) == 1


# Usage example
apple = RealString("Apple")
яблоко = RealString("Яблоко")

# Print
print(apple > яблоко)  # False
print(яблоко > apple)  # True
print(apple == яблоко)  # False
