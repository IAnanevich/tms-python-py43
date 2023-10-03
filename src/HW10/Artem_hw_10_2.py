class Share:
    def __init__(self, length_side: int, height: int) -> None:
        """

        :param length_side: int
        :param height: int
        """
        self.length_side = length_side
        self.height = height

    def area(self) -> None:
        """
        abstract method
        :return: Share area
        """
        raise NotImplementedError


class Triangle(Share):
    def area(self) -> float:
        """

        :return: Triangle area
        """
        return (self.length_side * self.height) / 2


class Rectangle(Share):
    def area(self) -> float:
        """

        :return: Rectangle area
        """
        return self.length_side * self.height


t = Triangle(length_side=3, height=5)
r = Rectangle(length_side=3, height=5)

print(f'Triangle area = {t.area()}')
print(f'Rectangle area = {r.area()}')
