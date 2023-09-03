"""Реализовать любой класс на свой выбор. В нем сделать:
конструктор, несколько методов (один обязательно статикметод, один классметод, один обычный)
переопределить один любой из магических методов (__lt__ и тд)
сделать один метод протектед. Сделать два класса дочерних. В этих классах переопределить все методы и
конструктор, которые можете (один метод должен быть переопределен ТОЛЬКО ОДИН раз в любом классе ребенке)
Сделать проверку, что все работает (создать обьекты от классов)"""


class Fruit:
    """
    class Fruit with attributes and methods
    Attributes: name, weight, color, shape
    Methods: __init__, call, price, receipt, __repr__, _protected
    """
    def __init__(self, name: str, weight: int | float, color: None = str, shape: None = str) -> None:
        """
        Makes a new class object.
        :param shape: shape
        :param name: name
        :param color: color
        :param weight: weight
        """
        self.name = name
        self.weight = weight

    @staticmethod
    def call() -> str:
        """
        A static method that returns a string
        :return: 'You have fruit'
        """
        return 'You have fruit'

    def price(self) -> int:
        """
        Returns the weight multiplied by 3
        :return: weight * 3
        """
        return self.weight * 3

    @classmethod
    def fruit_scale(cls, weight) -> str:
        """
        Class method returns 'too much' or 'normal'
        :return: string
        """
        if weight > 1400:
            return 'too much'
        return 'normal'

    def __repr__(self) -> str:
        """
        Returns a string with attribute name
        :return: string
        """
        return f'Fruit: {self.name}'

    @staticmethod
    def _protected() -> str:
        """
        A static method that returns a string
        :return: 'secret info'
        """
        return 'secret info'


class Apple(Fruit):
    def __init__(self, grown: str, quantity: int, name: str, weight: int, color: None = str, shape: None = str) -> None:
        """
        class Apple(parent = Fruit) with attributes and methods
        Attributes: grown, quantity, name, weight, color, shape
        Methods: __init__, call, price, receipt, __repr__, _protected
        :param grown: grown
        :param quantity: quantity
        :param name: name
        :param weight: weight
        :param color: color
        :param shape: shape
        """
        super().__init__(color, shape, name, weight)
        self.grown = grown
        self.name = name
        self.weight = weight
        self.quantity = quantity

    @staticmethod
    def call() -> str:
        """
        A static method that returns a string
        :return: 'You have apple'
        """
        return 'You have apple'

    def price(self) -> int:
        """
        Returns the weight and quantity multiplied by 3
        :return: weight * 3 * quantity
        """
        return self.weight * self.quantity * 3

    @classmethod
    def fruit_scale(cls, weight) -> str:
        """
        Class method returns 'too much' or 'normal'
        :return: string
        """
        if weight > 50:
            return 'too much'
        return 'normal'

    def __repr__(self) -> str:
        """
        Returns a string with attributes name and quantity
        :return: string
        """
        return f'Fruit: {self.name}, {self.quantity}'

    @staticmethod
    def _protected() -> str:
        """
        A static method that returns a string
        :return: 'more secret info'
        """
        return 'more secret info'


class Banana(Fruit):
    def __init__(self, company: str, name: str, weight: int | float, color: None = str, shape: None = str) -> None:
        """
        class Banana(parent = Fruit) with attributes and methods
        Attributes: company, name, weight, color, shape
        Methods: __init__, call, price, receipt, __repr__, _protected
        :param company: company
        :param name: name
        :param weight: weight
        :param color: color
        :param shape: shape
        """
        super().__init__(name, weight, color, shape)
        self.company = company
        self.name = name
        self.weight = weight

    @staticmethod
    def call() -> str:
        """
        A static method that returns a string
        :return: 'You have banana'
        """
        return 'You have banana'

    def price(self) -> int:
        """
        Returns the weight multiplied by 7
        :return: weight * 7
        """
        return self.weight * 7

    @classmethod
    def fruit_scale(cls, weight) -> str:
        """
        Class method returns 'too much' or 'normal'
        :return: string
        """
        if weight > 30:
            return 'too much'
        return 'normal'

    def __repr__(self) -> str:
        """
        Returns a string with attributes name and company
        :return: string
        """
        return f'Fruit: {self.name}, {self.company}'

    @staticmethod
    def _protected() -> str:
        """
        A static method that returns a string
        :return: 'the most secret info'
        """
        return 'the most secret info'


fruit_1 = Fruit(name='pamela', weight=452)
apple_1 = Apple(grown='China', name='apple golden', weight=145, quantity=4)
banana_1 = Banana(name='banana cavendish', company='Chiquita Brands International', weight=36)

print(fruit_1.call())
print(fruit_1.price())
print(fruit_1.fruit_scale(weight=1705))
print(fruit_1.__repr__())
print(fruit_1._protected())

print(20 * '-')

print(apple_1.call())
print(apple_1.price())
print(apple_1.fruit_scale(weight=35))
print(apple_1.__repr__())
print(apple_1._protected())

print(20 * '-')

print(banana_1.call())
print(banana_1.price())
print(banana_1.fruit_scale(weight=75))
print(banana_1.__repr__())
print(banana_1._protected())
