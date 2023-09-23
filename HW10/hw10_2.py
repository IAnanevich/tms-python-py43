# Cоздайте абстрактный класс геометрической фигуры Shape.
# С конструктором, принимающим длину стороны и высоту, проведенную к этой стороне.
class Shape:

    # Инициализация класса
    def __init__(self, width: float, height: float) -> None:
        self.width = width
        self.height = height

    # Определите в классе абстрактный метод area(),
    # который будет использоваться подклассами для расчета площади соответствующих им геометрических фигур.
    # Для реализации абстрактности метода используйте возбуждение исключения NotImplementedError.
    def area(self) -> float:
        """
        Абстрактный метод для расчета площади геометрических фигур
        :return: площадь фигуры
        """
        raise NotImplementedError("Необходимо переопределить метод при наследовании!")


# Далее создайте классы Triangle и Rectangle,
# наследующие суперкласс Shape и реализующие его абстрактный метод под свои нужды.
class Triangle(Shape):

    # Инициализация класса
    def __init__(self, width: float, height: float) -> None:
        super().__init__(width, height)

    def area(self) -> float:
        """
        Метод для расчета площади фигуры
        :return: площадь фигуры
        """
        return self.width * self.height / 2


class Rectangle(Shape):

    # Инициализация класса
    def __init__(self, width: float, height: float) -> None:
        super().__init__(width, height)

    def area(self) -> float:
        """
        Метод для расчета площади фигуры
        :return: площадь фигуры
        """
        return self.width * self.height


# Продемонстрируйте использование созданных классов для нахождения площади треугольника и прямоугольника
# по известным значениям длины стороны и высоты, проведенной к этой стороне.

tri = Triangle(width=10, height=22.5)
print(tri.area())

rect = Rectangle(width=10, height=22.5)
print(rect.area())
