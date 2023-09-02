# Строки в Питоне сравниваются на основании значений символов.
# Если мы захотим выяснить, что больше: «Apple» или «Яблоко» – то «Яблоко» окажется бОльшим.
# А все потому, что английская буква «A» имеет значение 65 (берется из таблицы кодировки).
# А русская буква «Я» – 1071 (с помощью функции ord() это можно выяснить).
#
# Такое положение дел не устроило Анну.
# Она считает, что строки нужно сравнивать по количеству входящих в них символов.
# Для этого девушка создала класс RealString и реализовала озвученный инструментарий.
# Сравнивать между собой можно как объекты класса, так и обычные строки с экземплярами класса RealString.
# К слову, Анне понадобилось только 3 метода внутри класса (включая __init__()) для воплощения задуманного.


# Сравнивать между собой можно как объекты класса, так и обычные строки с экземплярами класса RealString.
class RealString:

    def __init__(self, string: str):
        self.real_string = string

    def __gt__(self, other: any):
        return self.string_value(self) > self.string_value(other)

    @staticmethod
    def string_value(some_value: any):
        if isinstance(some_value, RealString):
            return len(some_value.real_string)
        try:
            return len(str(some_value))
        except ValueError:
            return -1


print(f"\nNormal string: АБВ > ABCD is {'АБВ' > 'ABCD'}")
print(f"Real string: RealString(АБВ) > RealString(ABCD) is {RealString(string='АБВ') > RealString(string='ABCD')}")
print(f"Real string: RealString(АБВ) > ABCD is {RealString(string='АБВ') > 'ABCD'}")
