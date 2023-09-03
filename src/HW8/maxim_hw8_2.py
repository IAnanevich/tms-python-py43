# Создать родительский класс auto, у которого есть атрибуты: brand, age, color, mark
# и weight. А так же методы: move, birthday и stop. Методы "move" и "stop" выводят
# сообщение на экран "move" и "stop", а birthday увеличивает атрибут age на 1.
# Атрибуты brand, age и mark являются обязательными при объявлении объекта.

class Auto:

    def __init__(self, brand: str, age: int, mark: str, color: str = "", weight: int | float = 0):
        self.brand = brand
        self.age = age
        self.color = color
        self.mark = mark
        self.weight = weight

    @staticmethod
    def move():
        print("move")

    @staticmethod
    def stop():
        print("stop")

    def birthday(self):
        self.age += 1
