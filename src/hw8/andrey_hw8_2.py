# Создать родительский класс auto, у которого есть атрибуты: brand, age, color, mark
# и weight. А так же методы: move, birthday и stop. Методы "move" и "stop" выводят
# сообщение на экран "move" и "stop", а birthday увеличивает атрибут age на 1.
# Атрибуты brand, age и mark являются обязательными при объявлении объекта.
class Auto:
    def __init__(self, brand: str, age: int, mark: str, color: str = '', weight: int = 0):
        self.age = age
        self.brand = brand
        self.mark = mark
        self.color = color
        self.weight = weight

    @staticmethod
    def move() -> None:
        """move"""
        print("move")

    @staticmethod
    def stop() -> None:
        """stop"""
        print("stop")

    def birthday(self) -> None:
        """increases age by 1"""
        self.age += 1
