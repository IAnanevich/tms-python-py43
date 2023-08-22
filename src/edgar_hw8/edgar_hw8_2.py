# Создать родительский класс Auto , у которого есть атрибуты: brand, age, color, mark и weight.
# А так же методы: move, birthday, stop. Методы move и stop выводят сообщения на экран "move" и "stop",
# а birthday увеличивает атрибут age на 1.
# Атрибут brand, age, mark являются обязательными при объявлении объекта.
# =============================================================================================================

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


car1 = Auto(brand="Toyota", age=5, mark="Camry", color="Blue", weight=1500)
car2 = Auto(brand="Honda", age=3, mark="Civic")

car1.move()
car2.birthday()
print(car2.age)
car1.stop()
