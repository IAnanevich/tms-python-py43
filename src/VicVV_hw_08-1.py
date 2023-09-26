# Создать класс RealString


class RealString:
    def __init__(self, string1) -> None:
        self.string1 = string1

    def __gt__(self, other) -> bool:
        return self.__len__() > other.__len__()

    def __lt__(self, other) -> bool:
        return self.__len__() < other.__len__()

    def __eq__(self, other) -> bool:
        return self.__len__() == other.__len__()

    def __len__(self) -> int:
        return self.string1.__len__()

    def __str__(self) -> str:
        return self.string1


s1 = RealString("dddd")
s2 = RealString("Zddd")
print(s1)
print(s1 == s2)
print(s1 < s2)
print(s1 == "Dddd")
print(".ddd" == s1)
