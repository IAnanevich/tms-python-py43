# Для рассмотренного на уроке класса Circle реализовать метод производящий
# вычитание двух окружностей, вычитание радиусов произвести по модулю. Если
# вычитаются две окружности с одинаковым значением радиуса, то результатом
# вычитания будет точка класса Point.
from math import pi


class Point(object):

    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __eq__(self, other):
        if isinstance(other, Point):
            return self.x == other.x and self.y == other.y
        else:
            return NotImplemented

    def __repr__(self):
        return f"Axis x: {self.x} and axis y: {self.y}"

    def __str__(self):
        return f"Point({self.x}, {self.y})"

    def distance_from_origin(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5


class Circle(Point):

    def __init__(self, x: int, y: int, radius: int):
        super().__init__(x, y)
        self.radius = radius

    def __eq__(self, other):
        if isinstance(other, Circle):
            return self.x == other.x and self.y == other.y and self.radius == other.radius
        else:
            return NotImplemented

    def __repr__(self):
        return f"Axis x: {self.x} and axis y: {self.y}, radius: {self.radius}"

    def __str__(self):
        return f"Circle(Point({self.x}, {self.y}), r={self.radius})"

    def edge_distance_from_origin(self):
        return abs(self.distance_from_origin() - self.radius)

    def area(self):
        return pi * self.radius ** 2

    def circumference(self):
        return 2 * pi * self.radius

    def __sub__(self, other):
        if isinstance(other, Circle):
            return Point(self.x, self.y) if self.radius == other.radius \
                else Circle(self.x - other.x, self.y - other.y, abs(self.radius - other.radius))
        else:
            return NotImplemented


if __name__ == "__main__":
    circle1 = Circle(9, 4, 10)
    circle2 = Circle(1, 2, 20)
    circle3 = Circle(5, 5, 20)
    print(f"{circle1} - {circle2} = {circle1 - circle2}")
    print(f"{circle2} - {circle3} = {circle2 - circle3}")
