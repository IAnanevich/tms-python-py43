'''Реализовать любой класс на свой выбор. В нем сделать: конструктор
несколько методов (один обязательно статикметод, один классметод, один обычный)
переопределить один любой из магических методов (__lt__ и тд) сделать один метод
протектед .Сделать два класса дочерних. В этих классах переопределить все методы
и конструктор, которые можете (один метод должен быть переопределен ТОЛЬКО ОДИН раз в любом классе ребенке)
Сделать проверку,что все работает (создать обьекты от классов)'''


class Figure:
    def __init__(self, color: str):
        '''
        Инициализирует объект класса Figure.

        :param color: цвет фигуры
        '''
        self.color = color

    @staticmethod
    def static_method():
        '''
        Статический метод класса Figure.
        '''
        print("This is a static method")

    @classmethod
    def class_method(cls):
        '''
        Метод класса Figure.
        '''
        print("This is a class method")

    def __lt__(self, other):
        '''
        Магический метод для сравнения двух объектов класса Figure по длине их цвета.

        :param other: другой объект класса Figure
        :return: True, если self.color меньше по длине, чем other.color, в противном случае False
        '''
        return len(self.color) < len(other.color)

    def _protected_method(self):
        '''
        Защищенный метод класса Figure.
        '''
        print("This is a protected method")


class Square(Figure):
    def __init__(self, color: str, side: int):
        '''
        Инициализирует объект класса Square.

        :param color: цвет квадрата
        :param side: длина стороны квадрата
        '''
        super().__init__(color)
        self.side = side

    def __str__(self) -> str:
        '''
        Возвращает строковое представление объекта класса Square.

        :return: строковое представление объекта класса Square
        '''
        return f"Square: color={self.color}, side={self.side}"


class Circle(Figure):
    def __init__(self, color: str, radius: float):
        '''
        Инициализирует объект класса Circle.

        :param color: цвет круга
        :param radius: радиус круга
        '''
        super().__init__(color)
        self.radius = radius

    def __str__(self) -> str:
        '''
        Возвращает строковое представление объекта класса Circle.

        :return: строковое представление объекта класса Circle
        '''
        return f"Circle: color={self.color}, radius={self.radius}"


# Проверка функциональности классов
square = Square("black", 5)
circle = Circle("orange", 3)

# Вызов общих методов и магического метода
square.static_method()
circle.class_method()
print(square < circle)

# Вызов переопределенных методов
square._protected_method()
circle._protected_method()
