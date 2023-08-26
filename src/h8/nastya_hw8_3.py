"""Строки в Питоне сравниваются на основании значений символов.
Т.е. если мы захотим выяснить, что больше: «Apple» или «Яблоко», – то «Яблоко» окажется бОльшим.
А все потому, что английская буква «A» имеет значение 65 (берется из таблицы кодировки),
а русская буква «Я» – 1071 (с помощью функции ord() это можно выяснить).
Такое положение дел не устроило Анну.
Она считает, что строки нужно сравнивать по количеству входящих в них символов.
Для этого девушка создала класс RealString и реализовала озвученный инструментарий. Сравнивать между собой
можно как объекты класса, так и обычные строки с экземплярами класса RealString.
К слову, Анне понадобилось только 3 метода внутри класса (включая __init__()) для воплощения задуманного."""


class RealString:
    """
    class RealString with attributes and methods
    Attributes: string_1, string_2
    Methods: check
    """
    def __init__(self, string_1, string_2):
        self.string_1 = string_1
        self.string_2 = string_2

    def check(self) -> None:
        """
        function checks which string is larger by the number of characters
        and writes the result of the check
        :return: None
        """
        try:
            if len(self.string_1) > len(self.string_2):
                print(f'{self.string_1} > {self.string_2}')
            elif len(self.string_1) < len(self.string_2):
                print(f'{self.string_1} < {self.string_2}')
            else:
                print(f'{self.string_1} = {self.string_2}')
        except TypeError:
            print('Try again(')


words = RealString('liluililuiluil', 'fgyju')
words.check()
