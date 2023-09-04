class RealString:
    def __init__(self, str_f: str) -> None:
        """

        :param str_f:
        """
        self.str_f = str_f

    def __lt__(self, other: str) -> bool:
        """

        :param other:
        :return: len(self.str_f) < len(other.str_f)
        """
        if not isinstance(other, RealString):
            other = RealString(other)
        return len(self.str_f) < len(other.str_f)

    def __gt__(self, other: str) -> bool:
        """

        :param other:
        :return: len(self.str_f) > len(other.str_f)
        """
        if not isinstance(other, RealString):
            other = RealString(other)
        return len(self.str_f) > len(other.str_f)


specified_lines_1 = RealString("kjjjj")
specified_lines_2 = RealString("hkhligt")
print(specified_lines_1 > "juhyjjjjjjg")
print(specified_lines_1 < specified_lines_2)
print("abc" < "adkkkkkkc")
