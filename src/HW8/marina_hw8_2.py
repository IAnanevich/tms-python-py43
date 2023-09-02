# Создать родительский класс auto, у которого есть атрибуты: brand, age, color, mark и weight.
# А также методы: move, birthday и stop. Методы move и stop выводят на экран сообщение 'move' и 'stop',
# а Birthday увеличивает атрибут age  на 1.
# Атрибуты brand, age и mark являются обязательными при объявлении объекта.


class Auto:
    """parents class"""

    def __init__(
        self, brand: str, age: int, mark: str, color: str = "", weight: int = 0
    ) -> None:
        """
        initialize attributes of class object
        :param brand: brand of the car
        :param age: age of the car
        :param mark: model of the car
        :param color: color of the car
        :param weight: weight of the car
        """
        self.brand = brand
        self.age = age
        self.color = color
        self.mark = mark
        self.weight = weight

    @staticmethod
    def move() -> None:
        """
        print message "move"
        """
        print("move")

    @staticmethod
    def stop() -> None:
        """
        print message "stop"
        """
        print("stop")

    def birthday(self) -> None:
        """
        increases age of object by 1
        """
        self.age += 1


carr = Auto(brand="opel", age=11, mark="astra", color="silver")

# проверяем метод move
carr.move()
# проверяем метод stop
carr.stop()
# проверяем метод birthday
print(f"Car age is {carr.age}")
carr.birthday()
print(f"Car age after its birthday is {carr.age}")
