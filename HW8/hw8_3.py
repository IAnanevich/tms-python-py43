from time import sleep


class Auto:
    def __init__(self, brand: str, age: int, mark: str, color: str = "no color", weight: float = 0):
        # Инициализация класса по параметрам
        self.brand = brand
        self.age = age
        self.color = color
        self.mark = mark
        self.weight = weight

    @staticmethod
    def move() -> None:
        """
        Движемся
        :return: Ничего
        """
        print("move")

    @staticmethod
    def stop() -> None:
        """
        Стоим
        :return: Ничего
        """
        print("stop")

    def birthday(self) -> None:
        """
        Увеличиваем возраст на 1
        :return: Ничего
        """
        self.age += 1


class Truck(Auto):
    def __init__(self, brand: str, age: int, mark: str, max_load: float, color: str = "no", weight: float = 0) -> None:
        # Инициализация класса по параметрам с вызовом инита из родительского класса
        super().__init__(brand=brand, age=age, mark=mark, color=color, weight=weight)
        self.max_load = max_load

    def move(self) -> None:
        """
        Внимание!
        :return: Ничего
        """
        print("attention")
        super().move()

    @staticmethod
    def load() -> None:
        """
        Грузимся
        :return: Ничего
        """
        sleep(1)
        print("load")
        sleep(1)


class Car(Auto):
    def __init__(self, brand: str, age: int, mark: str, max_speed: float, color: str = "no", weight: float = 0) -> None:
        # Инициализация класса по параметрам с вызовом инита из родительского класса
        super().__init__(brand=brand, age=age, mark=mark, color=color, weight=weight)
        self.max_speed = max_speed

    def move(self) -> None:
        """
        Движемся
        :return: Ничего
        """
        super().move()
        print(f"Max speed is {self.max_speed}")


my_truck = Truck(brand="truck brand 1", age=40, mark="truck mark 1", max_load=1000, color="pi color", weight=1.5)
my_truck.move()
my_truck.load()
my_truck.stop()
my_truck.birthday()
print(my_truck.brand, my_truck.age, my_truck.mark, my_truck.color, my_truck.weight, my_truck.max_load)

my_truck = Truck(brand="truck brand 2", age=20, mark="truck mark 2", max_load=2000)
print(my_truck.brand, my_truck.age, my_truck.mark, my_truck.color, my_truck.weight, my_truck.max_load)

my_car = Car(brand="some brand 1", age=30, mark="some mark 1", max_speed=60, color="ye color", weight=250)
my_car.move()
my_car.stop()
my_car.birthday()
print(my_truck.brand, my_truck.age, my_truck.mark, my_truck.color, my_truck.weight, my_truck.max_load)

my_car = Car(brand="some brand 2", age=50, mark="some mark 2", max_speed=90)
my_car.move()
print(my_truck.brand, my_truck.age, my_truck.mark, my_truck.color, my_truck.weight, my_truck.max_load)
