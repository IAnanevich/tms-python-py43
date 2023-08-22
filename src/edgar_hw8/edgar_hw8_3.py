# Создать два класса truck & car, которые являются наследниками класса auto. Класс truck имеет дополнительный
# обязательный атрибут max_load. Переопределнный метод move, перед появлением надписи "move" выводить
# "attention", его реализацию сделать при помощи оператора super. А так же дополнительный метод load
# При его вызове происходит пауза 1 сек., затем выдается сообщение "load", и снова пауза 1 сек.
# Класс car имеет дополнительный обязательный атрибут max_speed и при вызове метода move, после появления надписи
# "move" должна появиться надпись "max speed is <max_speed>".
# Создать по два объекта для каждого из классов truck & car, проверить все их методы и атрибуты
# ================================================================================================================

from time import sleep


class Auto:
    """
    A class representing an automobile.

    Attributes:
        brand (str): The brand of the automobile.
        age (int): The age of the automobile in years.
        mark (str): The mark of the automobile.
        color (str, optional): The color of the automobile.
        weight (float, optional): The weight of the automobile in kilograms.
    """

    def __init__(self, brand: str, age: int, mark: str, color: str = "", weight: float = 0.0):
        """
         Initialize a new Auto object.

        Args:
            :param brand: The brand of the automobile.
            :param age: The age of the automobile in years.
            :param mark: The mark of the automobile.
            :param color: The color of the automobile.
            :param weight: The weight of the automobile in kilograms.
        """

        self.brand = brand
        self.age = age
        self.mark = mark
        self.color = color
        self.weight = weight

    def move(self) -> None:
        """
         Print a message indicating that the automobile is moving.
        """
        print("move")

    def birthday(self) -> None:
        """
        Increase the age of the automobile by 1 year.
        """
        self.age += 1

    def stop(self) -> None:
        """
        Print a message indicating that the automobile has stopped.
        """
        print("stop")


class Truck(Auto):
    """
    A class representing a truck, inheriting from Auto.

    Attributes:
        max_load (float): The maximum load capacity of the truck in kilograms.
    """

    def __init__(self, brand: str, age: int, mark: str, max_load: float, color: str = "", weight: float = 0.0):
        """
        Initialize a new Truck object.

        Args:
            brand (str): The brand of the truck.
            age (int): The age of the truck in years.
            mark (str): The mark of the truck.
            max_load (float): The maximum load capacity of the truck in kilograms.
            color (str, optional): The color of the truck.
            weight (float, optional): The weight of the truck in kilograms.
        """
        super().__init__(brand, age, mark, color, weight)
        self.max_load = max_load

    def move(self) -> None:
        """
        Print a message indicating that the truck is moving with "attention" before "move".
        """
        print("attention")
        super().move()

    def load(self) -> None:
        """
        Simulate loading the truck with a pause and a message.
        """
        sleep(1)
        print("load")
        sleep(1)


class Car(Auto):
    """
    A class representing a car, inheriting from Auto.

    Attributes:
        max_speed (float): The maximum speed of the car in km/h.
    """

    def __init__(self, brand: str, age: int, mark: str, max_speed: float, color: str = "", weight: float = 0.0):
        """
        Initialize a new Car object.

        Args:
            brand (str): The brand of the car.
            age (int): The age of the car in years.
            mark (str): The mark of the car.
            max_speed (float): The maximum speed of the car in km/h.
            color (str, optional): The color of the car.
            weight (float, optional): The weight of the car in kilograms.
        """
        super().__init__(brand, age, mark, color, weight)
        self.max_speed = max_speed

    def move(self) -> None:
        """
        Print a message indicating that the car is moving and its maximum speed.
        """
        super().move()
        print(f"max speed is {self.max_speed} km/h")


# Creating instances of Truck
truck1 = Truck("Mercedes", 3, "TruckMark", 5000)
truck2 = Truck("Volvo", 5, "TruckMark", 7000)

# Creating instances of Car
car1 = Car("Toyota", 2, "CarMark", 180)
car2 = Car("BMW", 4, "CarMark", 220)

# Testing methods and attributes
truck1.move()
truck1.load()
truck1.stop()
print(f"Truck brand: {truck1.brand}, Max Load: {truck1.max_load}")

car2.move()
car2.birthday()
print(f"Car age: {car2.age}")
