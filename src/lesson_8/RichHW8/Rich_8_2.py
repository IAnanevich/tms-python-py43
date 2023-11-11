"""
Создать два класса truck & car, которые являются наследниками класса auto.
Класс truck имеет дополнительный обязательный атрибут max_load.
Переопределенный метод move, перед появлением надписи "move" выводить "attention", его реализацию сделать при помощи
оператора super.
А так же дополнительный метод load. При его вызове происходит пауза 1 сек., затем выдается сообщение "load",
и снова пауза 1 сек.
Класс car имеет дополнительный обязательный атрибут max_speed и при вызове метода move, после появления надписи "move"
должна появиться надпись "max speed is <max_speed>".
Создать по два объекта для каждого из классов truck & car, проверить все их методы и атрибуты.
"""
import time


class Auto:
    def __init__(
            self, brand: str, age: int = 1, mark: str = 'st', color: str = "", weight: int = 0) -> None:
        """
        :param brand: str
        :param age: int
        :param mark: str
        :param color: str
        :param weight: int
        """
        self.brand = brand
        self.age = age
        self.color = color
        self.mark = mark
        self.weight = weight

    @staticmethod
    def move() -> None:
        """
        print 'move'
        :return:
        """
        print("move")

    @staticmethod
    def stop() -> None:
        """
        print 'stop'
        :return:
        """
        print("stop")

    def birthday(self) -> None:
        """
        increasing the age of the automobile by 1
        :return:
        """
        self.age += 1


car_one = Auto("mazda", 7, "ford")
car_one.move()
car_one.stop()
car_one.birthday()
print(f"Brand: {car_one.brand}")
print(f"Age: {car_one.age} years")
print(f"Color: {car_one.color}")
print(f"Mark: {car_one.mark}")
print(f"Weight: {car_one.weight} kg")


class Truck(Auto):
    def __init__(
            self,
            brand: str,
            age: int,
            mark: str,
            color: str,
            weight: int,
            max_load: int
    ):
        super().__init__(self, brand, age, mark, color, weight)
        self.max_load = max_load

    def move(self):
        """
        print attention
        :return:
        """
        print("attention")
        super().move()

    @staticmethod
    def load():
        """
        time +1 sec and print 'loading'
        :return:
        """
        time.sleep(1)
        print('Loading')
        time.sleep(1)


class Car(Auto):
    def __init__(
            self,
            brand=str,
            age=int,
            mark=str,
            color=str,
            weight=int,
            max_speed=int,
    ):
        super().__init__(self, brand, age, mark, color, weight)
        self.max_load = max_speed()

    def move(self):
        """
        print max speed
        :return:
        """
        max_speed = int()
        super().move()
        print(f"Max speed  {max_speed}")


car_one = Auto("mazda", 7, "ford")
car_one.move()
car_one.stop()
car_one.birthday()
print(f"Brand: {car_one.brand}")
print(f"Age: {car_one.age} years")
print(f"Color: {car_one.color}")
print(f"Mark: {car_one.mark}")
print(f"Weight: {car_one.weight} kg")
