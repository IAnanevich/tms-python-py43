"""2. Создать 2 класса truck и car, которые являются наследниками класса auto.
Класс truck имеет дополнительный обязательный атрибут max_load.
Переопределённый метод move, перед появлением надписи «move» выводит надпись «attention»,
его pеализацию сделать при помощи оператора super. А так же дополнительный метод load.
При его вызове происходит пауза 1 сек. , затем выдаётся сообщение «load» и снова пауза 1 сек.
Класс car имеет дополнительный обязательный атрибут max_speed и при вызове метода move, после появления
надписи «move» должна появиться надпись «max speed is <max_speed>». Создать по 2 объекта для каждого из
классов truck и car, проверить все их методы и атрибуты."""
import time


class Auto:
    """
    class Auto with attributes and methods
    Attributes: brand, age, mark, color, weight
    Methods: stop, move, birthday
    """
    def __init__(self, brand: str, age: int, mark: str, color: None = str, weight: None = int):
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


class Truck(Auto):
    """
    parent class Auto
    class Truck with attributes and methods
    Attributes: brand, age, mark, max_load, color, weight
    Methods: stop, move, birthday, load
    """
    def __init__(self, brand: str, age: int, mark: str, max_load: int, color: str = None, weight: int = None):
        """
        Makes a new class object.
        :param brand: brand
        :param age: age
        :param mark: mark
        :param max_load: max_load
        :param color: color
        :param weight: weight
        """
        super().__init__(brand, age, mark, color=None, weight=None)

    @staticmethod
    def move() -> None:
        """
        writes attention
        :return: None
        """
        print('attention')

    @staticmethod
    def load() -> None:
        """
        waits 1 sec
        writes load
        waits 1 sec
        :return: None
        """
        time.sleep(1)
        print('load')
        time.sleep(1)


class Car(Auto):
    """
    parent class Auto
    class Car with attributes and methods
    Attributes: max_speed, brand, age, mark, color, weight
    Methods: stop, move, birthday
    """
    def __init__(self, max_speed, brand, age, mark, color=None, weight=None):
        """
        Makes a new class object.
        :param max_speed: max_speed
        :param brand: brand
        :param age: age
        :param mark: mark
        :param color: color
        :param weight: weight
        """
        super().__init__(brand, age, mark, color=None, weight=None)
        self.max_speed = max_speed

    def move(self) -> None:
        """
        writes max speed
        :return: None
        """
        print(f'max speed is {self.max_speed}')


mer = Truck('Mercedes', 10, 'Benz', 5254)
sca = Truck('Scania', 12, 'AB', 5771)
ford = Car(120, 'Ford', 6, 'Aero')
bmw = Car(98, 'BMW', 4, 'Mini')
mer.move()
mer.load()
mer.stop()
mer.birthday()
sca.move()
sca.load()
sca.stop()
sca.birthday()
ford.move()
ford.birthday()
ford.stop()
bmw.move()
bmw.birthday()
bmw.stop()
