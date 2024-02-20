# Создайте абстрактный класс геометрической фигуры Shape с конструктором,
# принимающим длину стороны и высоту, проведенную к этой стороне.
# Определите в классе абстрактный метод area(), который будет использоваться подклассами
# для расчета площади соответствующих им геометрических фигур.
# Для реализации абстрактности метода используйте возбуждение исключения NotImplementedError.
# Создайте классы Triangle и Rectangle, наследующие супер класс Shape и реализующие его
# абстрактный метод под свои нужды. Продемонстрируйте использование созданных классов для нахождения площади
# треугольника и прямоугольника по известным значениям длины стороны и высоты, проведенной к этой стороне.
from abc import ABC


class Shape(ABC):
    """
    abstract class of figure
    """

    def __init__(self, base_figure: int | float, height_to_base: int | float) -> None:
        """
        initialisation
        :param base_figure: base of figure
        :param height_to_base: height to base to find area of figure
        """
        self.base_figure = base_figure
        self.height_to_base = height_to_base

    def area(self) -> float:
        """
        find area of figure
        :return: float number - area of figure
        """
        raise NotImplementedError("need to adaptation method 'area'")


class Triangle(Shape):
    """
    child-class of Shape with triangles
    """

    def area(self) -> float:
        """
        find area of triangle
        :return: area of triangle
        """
        return 0.5 * self.base_figure * self.height_to_base


class Rectangle(Shape):
    """
    child-class of Shape with rectangles
    """

    def area(self) -> float:
        """
        find area of rectangle
        :return: area of rectangle
        """
        return self.base_figure * self.height_to_base


class Circle(Shape):
    """
    child-class for check Exception in Shape
    """

    @staticmethod
    def sey() -> None:
        """
        display Hello
        :return: None
        """
        print("Hello")


# проверка для треугольника
triangle_1 = Triangle(base_figure=5, height_to_base=4)
try:
    print(f"Area of triangle is: {triangle_1.area()}")
except NotImplementedError as error:
    print(f"Class {triangle_1.__class__.__name__}: {error}")
#
# проверка для прямоугольника
rectangle_1 = Rectangle(base_figure=4.5, height_to_base=4)
try:
    print(f"Area of rectangle is: {rectangle_1.area()}")
except NotImplementedError as error:
    print(f"Class {rectangle_1.__class__.__name__}: {error}")
#
# проверка на исключение
circle_1 = Circle(base_figure=4.5, height_to_base=4)
try:
    print(f"Area of rectangle is: {circle_1.area()}")
except NotImplementedError as error:
    print(f"Class {circle_1.__class__.__name__}: {error}")
