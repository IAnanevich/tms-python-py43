# Создать родительский класс Auto, у которого есть Атрибуты: brand, age, color, mark, weight.
# Методы move, bithday, stop.
# Методы  "move" и "stop" выводят сообщения на экран "move" и "stop", а birthday увеличивает атрибут age на 1.
# Атрибуты brand, age и mark обязательные при объявлении объекта.


class Auto:
    def __init__(
            self, brand: str, age: int = 1, mark: str = 'st', color: str = "", weight: float = 0) -> None:
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
