# Создать 2 класса Truck и car, которые являются наследниками класса auto.
# Класс truck имеет дополнительный обязательный атрибут max_load.
# Переопределенный метод move перед появлением надписи move выводит надпись attention,
# и дополнительный метод Load:
# при его вызове происходит пауза 1 сек, затем выдается сообщение load и снова пауза 1 секунда.
# Класс Car имеет дополнительный обязательный атрибут max_speed и при вызове метода move,
# после появления надписи move должна появиться надпись "max_speed is <max_speed>".
# Создать по 2 объекта для каждого из классов truck и car, проверить все методы и атрибуты.
#
from time import sleep


class Auto:
    """parents class"""

    def __init__(
        self, brand: str, age: int, mark: str, color: str = "", weight: int = 0
    ):
        self.brand = brand
        self.age = age
        self.color = color
        self.mark = mark
        self.weight = weight

    @staticmethod
    def move():
        """
        print message "move"
        """
        print("move")

    @staticmethod
    def stop():
        """
        print message "stop"
        """
        print("stop")

    def birthday(self):
        """
        increases age of object by 1
        """
        self.age += 1


class Truck(Auto):
    def __init__(
        self,
        brand: str,
        age: int,
        mark: str,
        max_load: int,
        color: str = "",
        weight: int = 0,
    ):
        super().__init__(brand, age, mark, color, weight)
        self.max_load = max_load

    @staticmethod
    def move():
        """
        print message "Attention" ann after that print "move"
        """
        print("Attention\nmove")

    @staticmethod
    def load():
        """
        make 1-second-break, print 'load', make another 1-second-break,
        """
        sleep(1)
        print("load")
        sleep(1)


class Car(Auto):
    def __init__(
        self,
        brand: str,
        age: int,
        mark: str,
        max_speed: int,
        color: str = "",
        weight: int = 0,
    ):
        super().__init__(brand, age, mark, color, weight)
        self.max_speed = max_speed

    def move(self):
        print(f"move \nmax_speed is <{self.max_speed}>")


# объекты класса Truck
truck_1 = Truck("Volvo", 10, "FH16", 35)
truck_2 = Truck("Daf", 2, "CF85", 32, "silver", 8)
# объекты класса Car
car_1 = Car("Lamborghini", 5, "Aventador", 350, "black", 1625)
car_2 = Car("Opel", 12, "Astra", 244)

# проверка методов и атрибутов класса Track
print(f"Info truck_1\n{truck_1.__dict__}")
print(f"Info truck_2\n{truck_2.__dict__}")
print('Result of method "move" in class Track:')
truck_1.move()
print('Result of method "stop" in class Track:')
truck_1.stop()
truck_2.birthday()
print(f"Changed Info age truck_2:\n{truck_2.age}")
print('Result of method "move" in class Track:')
truck_2.load()
# проверка методов и атрибутов класса Car
print(f"Info car_1\n{car_1.__dict__}")
print(f"Info car_2\n{car_2.__dict__}")
print('Result of method "move" in class Car:')
car_1.move()
print('Result of method "stop" in class Car:')
car_1.stop()
car_2.birthday()
print(f"Changed Info age car_2:\n{car_2.age}")
