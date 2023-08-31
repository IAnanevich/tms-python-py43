'''Реализовать любой класс на свой выбор. В нем сделать: конструктор
несколько методов (один обязательно статикметод, один классметод, один обычный)
переопределить один любой из магических методов (__lt__ и тд) сделать один метод
протектед .Сделать два класса дочерних. В этих классах переопределить все методы
и конструктор, которые можете (один метод должен быть переопределен ТОЛЬКО ОДИН раз в любом классе ребенке)
Сделать проверку, что все работает (создать обьекты от классов)'''


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height

    def is_square(self):
        return self.width == self.height

    def print_info(self):
        print("Width:", self.width)
        print("Height:", self.height)
        print("Area:", self.calculate_area())

    @staticmethod
    def get_smallest_side(width, height):
        return min(width, height)

    @classmethod
    def create_square(cls, side):
        return cls(side, side)

    def __str__(self):
        return f"Rectangle: {self.width} x {self.height}"


class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)

    def calculate_area(self):
        return self.width ** 2

    def is_square(self):
        return True

    def print_info(self):
        print("Side:", self.width)
        print("Area:", self.calculate_area())


class ExtendedRectangle(Rectangle):
    def __init__(self, width, height):
        super().__init__(width, height)

    def calculate_area(self):
        return super().calculate_area() * 2

    def is_large_rectangle(self):
        return self.calculate_area() > 100


# Create objects and test
rect = Rectangle(5, 10)
rect.print_info()
print("Is square?", rect.is_square())
print("Smallest side:", Rectangle.get_smallest_side(rect.width, rect.height))
print(rect)

print()

square = Square(7)
square.print_info()
print("Is square?", square.is_square())
print("Smallest side:", Rectangle.get_smallest_side(square.width, square.height))
print(square)

print()

extended_rect = ExtendedRectangle(3, 15)
extended_rect.print_info()
print("Is square?", extended_rect.is_square())
print("Smallest side:", Rectangle.get_smallest_side(extended_rect.width, extended_rect.height))
print("Is large rectangle?", extended_rect.is_large_rectangle())
print(extended_rect)
