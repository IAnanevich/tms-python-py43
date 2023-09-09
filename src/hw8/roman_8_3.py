'''Создать два класса truck & car, которые являются наследниками класса auto. Класс truck имеет дополнительный
обязательный атрибут max_load. Переопределнный метод move, перед появлением надписи "move" выводить
"attention", его реализацию сделать при помощи оператора super. А так же дополнительный метод load
При его вызове происходит пауза 1 сек., затем выдается сообщение "load", и снова пауза 1 сек.
Класс car имеет дополнительный обязательный атрибут max_speed и при вызове метода move,
после появления надписи "move" должна появиться надпись "max speed is <max_speed>".
Создать по два объекта для каждого из классов truck & car, проверить все их методы и атрибуты'''

import time


class Auto:
    def __init__(self, brand: str, age: int, mark: str, color: str = "", weight: float = 0.0) -> None:
        """Создает объект автомобиля

        Args:
            brand (str): Марка автомобиля
            age (int): Возраст автомобиля
            mark (str): Модель автомобиля
            color (str, optional): Цвет автомобиля. По умолчанию "".
            weight (float, optional): Вес автомобиля. По умолчанию 0.0.
        """
        self.brand = brand
        self.age = age
        self.mark = mark
        self.color = color
        self.weight = weight

    def move(self) -> None:
        """Запускает движение автомобиля"""
        print("move")

    def birthday(self) -> None:
        """Увеличивает возраст автомобиля на 1"""
        self.age += 1

    def stop(self) -> None:
        """Останавливает автомобиль"""
        print("stop")


class Truck(Auto):
    def __init__(self, brand: str, age: int, mark: str, max_load: int, color: str = "", weight: float = 0.0) -> None:
        """Создает объект грузовика

        Args:
            brand (str): Марка грузовика
            age (int): Возраст грузовика
            mark (str): Модель грузовика
            max_load (int): Максимальная грузоподъемность грузовика
            color (str, optional): Цвет грузовика. По умолчанию "".
            weight (float, optional): Вес грузовика. По умолчанию 0.0.
        """
        super().__init__(brand, age, mark, color, weight)
        self.max_load = max_load

    def move(self) -> None:
        """Запускает движение грузовика"""
        print("attention")
        super().move()

    def load(self) -> None:
        """Загружает грузовик"""
        time.sleep(1)
        print("load")
        time.sleep(1)


class Car(Auto):
    def __init__(self, brand: str, age: int, mark: str, max_speed: int, color: str = "", weight: float = 0.0) -> None:
        """Создает объект легкового автомобиля

        Args:
            brand (str): Марка автомобиля
            age (int): Возраст автомобиля
            mark (str): Модель автомобиля
            max_speed (int): Максимальная скорость автомобиля
            color (str, optional): Цвет автомобиля. По умолчанию "".
            weight (float, optional): Вес автомобиля. По умолчанию 0.0.
        """
        super().__init__(brand, age, mark, color, weight)
        self.max_speed = max_speed

    def move(self) -> None:
        """Запускает движение легкового автомобиля"""
        super().move()
        print("max speed is", self.max_speed)


truck1 = Truck("МАЗ", 32, "51021", max_load=1900, color="Gray", weight=5300)
truck2 = Truck("УАЗ", 54, "Буханка", max_load=4000, color="Silver", weight=1200)
car1 = Car("RAM", 3, "TRX", max_speed=220, color="Black", weight=3000)
car2 = Car("Mersedes", 10, "CLS", max_speed=300, color="Black", weight=1700)

print(truck1.brand)
print(truck1.age)
print(truck1.color)
truck1.move()
truck1.load()
truck1.stop()

print()

print(car1.brand)
print(car2.age)
print(car2.color)
car2.move()
car2.stop()
