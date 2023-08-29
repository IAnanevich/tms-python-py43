# Создать 2 класса truck и car, которые является наследниками класса auto. Класс
# truck имеет дополнительный обязательный атрибут max_load. Переопределенный
# метод move, перед появлением надписи "move" выводит надпись "attention", его
# реализацию сделать при помощи оператора super. А так же дополнительный метод
# load. При его вызове происходит пауза 1 сек., затем выдаётся сообщение "load" и
# снова пауза 1 сек. Класс car имеет дополнительный обязательный атрибут
# max_speed и при вызове метода move, после появления надписи "move" должна
# появиться надпись "max_speed is <max_speed>". Создать по 2 объекта для каждого
# из классов truck car, проверить все их методы и атрибуты.

import time


class Auto():
    """
    parent class "Auto" with two children classes: "Car" and "Truck"
    """

    def __init__(self, brand: str, age: int, color: str, mark: str, weight: int) -> None:
        """

        :param brand: str
        :param age: int
        :param color: str
        :param mark: str
        :param weight: int
        """
        self.brand = brand
        self.age = age
        self.color = color
        self.mark = mark
        self.weight = weight

    def move(self) -> None:
        """
        print "move"
        :return:
        """
        print('move')

    def stop(self) -> None:
        """
        print "stop"
        :return:
        """
        print('stop')

    def berthday(self) -> None:
        """
        adds one year to the age of the car
        :return:
        """
        self.age += 1


class Truck(Auto):
    """
    child class "Truck" from "Auto" class
    """

    def __init__(self, brand: str, age: int, color: str, mark: str, weight: int, max_load: int) -> None:
        """

        :param brand:
        :param age:
        :param color:
        :param mark:
        :param weight:
        :param max_load:
        """
        super().__init__(brand, age, color, mark, weight)
        self.max_load = max_load

    def move(self) -> None:
        """
        before the "move" appears, it displays the inscription "attention"
        :return: move after attention
        """
        print('attention')
        super().move()

    def stop(self):
        """
        print "stop"
        :return:
        """
        print('stop')

    def birthday(self):
        """
        adds one year to the age of the car
        :return:
        """
        self.age += 1

    def load(self):
        """
        1-second delay, output message "load", 1-second delay
        :return:
        """
        time.sleep(1)
        print('load')
        time.sleep(1)


class Car(Auto):
    """
    child class "Car" from "Auto" class
    """

    def __init__(self, brand: str, age: int, color: str, mark: str, weight: int, max_speed: int) -> None:
        """

        :param brand:
        :param age:
        :param color:
        :param mark:
        :param weight:
        :param max_speed:
        """
        super().__init__(brand, age, color, mark, weight)
        self.max_speed = max_speed

    def move(self) -> None:
        """
        notification of the maximum speed of the car
        :return:
        """
        super().move()
        print(f'max speed is {self.max_speed}')

    def stop(self) -> None:
        """
        print "stop"
        :return:
        """
        print('stop')

    def birthday(self) -> None:
        """
        adds one year to the age of the car
        :return:
        """
        self.age += 1


car_1 = Car(brand='BMW', age=2, color='black', mark='m340i', weight=1710, max_speed=276)
car_2 = Car(brand='Nissan', age=21, color='blue', mark='gt-r34', weight=1550, max_speed=250)

truck_1 = Truck(brand='MAN', age=11, color='white', mark='TGS', weight=7300, max_load=18000)
truck_2 = Truck(brand='Volvo', age=5, color='green', mark='FH', weight=8100, max_load=22000)

car_1.move()
car_1.stop()
car_1.birthday()
print(f'brand {car_1.brand}')
print(f'age {car_2.age}')
print('___________')
truck_1.move()
truck_1.stop()
truck_1.birthday()
print(f'max load is {truck_2.max_load}')
truck_1.load()
print(f'age is {truck_2.age}')
