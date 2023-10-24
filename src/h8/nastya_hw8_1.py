"""1. Создать родительский класс auto, у которого есть атрибуты: brand, age, color, mark и weight.
 А так же методы: move, birthday и stop. Методы move и stop выводят сообщение на экран «move» и «stop»,
 a birthday увеличивает атрибут age на 1. Атрибуты brand, age и mark являются обязательными при объявлении
 объекта."""


class Auto:
    """
    class Auto with attributes and methods
    Attributes: brand, age, mark, color, weight
    Methods: stop, move, birthday
    """
    def __init__(self, brand: str, age: int, mark: str, color: None = str, weight: None = int) -> None:
        """
        Makes a new class object.
        :param brand: brand
        :param age: age
        :param mark: mark
        :param color: color
        :param weight: weight
        """
        self.age = age

    def birthday(self) -> None:
        """
        func adds 1 to the age of the car
        :return: None
        """
        print(self.age + 1)

    @staticmethod
    def stop() -> None:
        """
        func writes 'stop'
        :return: None
        """
        print('stop')

    @staticmethod
    def move() -> None:
        """
        func writes 'move'
        :return: None
        """
        print('move')
