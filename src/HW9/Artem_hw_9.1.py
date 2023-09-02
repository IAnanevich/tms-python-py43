# Реализовать любой класс на свой выбор. В нем сделать:
# конструктор
# несколько методов (один обязательно статикметод, один классметод, один обычный)
# переопределить один любой из магических методов (__lt__ и тд)
# сделать один метод протектед

from Artem_hw_9_3 import Number


class Arithmetic:
    string = 'Сalculator'

    def __init__(self, x: Number) -> None:
        """

        :param x: int
        """
        self.x = x

    @staticmethod
    def mathematics() -> None:
        """
        static method of the Arithmetic class
        :return: None
        """
        print('math')

    @classmethod
    def calculate(cls) -> None:
        """
        class method of the Arithmetic class
        :return: None
        """
        print(f'{cls.string}')

    def __add__(self, other) -> None:
        """
        addition method
        :param other: class object
        :return: x + other
        """
        check = other if isinstance(other, int) else other.x
        return print(f'add: {self.x + check}')

    def _protected(self) -> None:
        """

        :return: none
        """
        return print("protected method")

    def __sub__(self, other) -> None:
        """
        subtraction method
        :param other: class object
        :return: x - other
        """
        check = other if isinstance(other, int) else other.x
        return print(f'sub: {self.x - check}')


class Algebra(Arithmetic):
    def __init__(self, y: int) -> None:
        """

        :param y: int
        """
        super().__init__(y)
        self.y = y

    def __mul__(self, other):
        """
        multiplication method
        :param other: class object
        :return: y * other
        """
        check = other if isinstance(other, int) else self.y
        return print(f'mul: {self.y * check}')

    def __truediv__(self, other):
        """
        division method
        :param other: class object
        :return: y / other
        """
        check = other if isinstance(other, int) else self.y
        return print(f'div: {self.y / check}')


class Compare(Arithmetic):
    def __init__(self, comp: int) -> None:
        """

        :param comp: int
        """
        super().__init__(comp)
        self.comp = comp

    def __gt__(self, other) -> None:
        """
        comp and other comparisons
        :param other: class object
        :return: True if "comp" > than "other"
        """
        check = other if isinstance(other, int) else self.comp
        return print(f'bool: {self.comp > check}')


arithmetic = Arithmetic(x=10)
algebra = Algebra(y=6)
compare = Compare(comp=30)

algebra._protected()
compare._protected()
arithmetic.calculate()
arithmetic.mathematics()
arithmetic.__add__(other=12)
arithmetic.__sub__(other=12)
algebra.__mul__(other=12)
algebra.__truediv__(other=12)
compare.__gt__(other=9)