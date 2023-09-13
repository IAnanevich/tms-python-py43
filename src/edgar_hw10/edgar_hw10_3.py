# Cоздайте абстрактный класс геометрической фигуры Shape с конструктором,
# принимающим длину стороны и высоту, проведенную к этой стороне.
# Определите в классе абстрактный метод area(), который будет использоваться
# подклассами для расчета площади соответствующих им геометрических фигур.
# Для реализации абстрактности метода используйте возбуждение исключения NotImplementedError.
# Далее создайте классы Triangle и Rectangle, наследующие суперкласс Shape и реализующие
# его абстрактный метод под свои нужды. Продемонстрируйте использование
# созданных классов для нахождения площади треугольника и прямоугольника
# по известным значениям длины стороны и высоты, проведенной к этой стороне.

from abc import ABC, abstractmethod


class Shape(ABC):
    def __init__(self, side_length: float, height: float) -> None:
        """
        Инициализирует геометрическую фигуру.

        :param side_length: Длина стороны фигуры.
        :param height: Высота, проведенная к стороне.
        """
        self.side_length = side_length
        self.height = height

    @abstractmethod
    def area(self) -> float:
        """
        Абстрактный метод для расчета площади геометрической фигуры.
        """
        pass


class Triangle(Shape):
    def area(self) -> float:
        """
        Рассчитывает площадь треугольника.

        :return: Площадь треугольника.
        """
        return 0.5 * self.side_length * self.height


class Rectangle(Shape):
    def area(self) -> float:
        """
        Рассчитывает площадь прямоугольника.

        :return: Площадь прямоугольника.
        """
        return self.side_length * self.height


try:
    triangle = Triangle(side_length=5, height=4)
    rectangle = Rectangle(side_length=6, height=8)

    print(f"Площадь треугольника: {triangle.area()}")
    print(f"Площадь прямоугольника: {rectangle.area()}")
except Exception as e:
    print(f"Ошибка: {e}")
