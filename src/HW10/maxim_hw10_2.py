# Cоздайте абстрактный класс геометрической фигуры Shape с конструктором,
# принимающим длину стороны и высоту, проведенную к этой стороне.
# Определите в классе абстрактный метод area(), который будет использоваться
# подклассами для расчета площади соответствующих им геометрических фигур.
# Для реализации абстрактности метода используйте возбуждение исключения NotImplementedError.
# Далее создайте классы Triangle и Rectangle, наследующие суперкласс Shape и реализующие
# его абстрактный метод под свои нужды. Продемонстрируйте использование
# созданных классов для нахождения площади треугольника и прямоугольника
# по известным значениям длины стороны и высоты, проведенной к этой стороне.


class Shape:
    """ Abstract geometric shape class """

    def __init__(self, width: int | float, height: int | float) -> None:
        self.width, self.height = width, height

    def area(self) -> float:
        """ Abstractness of the figure area method

        :return: the area of the figure
        """
        raise NotImplementedError("This is an abstract method")


class Triangle(Shape):
    def __init__(self, width: int | float, height: int | float) -> None:
        super().__init__(width, height)

    def area(self) -> float:
        """ Return the area of the triangle

        :return: the area of the triangle
        """
        return self.width * self.height / 2


class Rectangle(Shape):
    def __init__(self, width: int | float, height: int | float) -> None:
        super().__init__(width, height)

    def area(self) -> float:
        """ Return the area of the rectangle

        :return: the area of the rectangle
        """
        return self.width * self.height


if __name__ == "__main__":
    value_width = float(input("Enter a width value: "))
    value_height = float(input("Enter a height value: "))
    triangle = Triangle(value_width, value_height)
    rectangle = Rectangle(value_width, value_height)
    shape = Shape(value_width, value_height)
    print(triangle.area())
    print(rectangle.area())
    print(shape.area())
