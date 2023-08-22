''' Создать родительский класс Auto , у которого есть атрибуты: brand, age, color, mark и weight.
А так же методы: move, birthday, stop. Методы move и stop выводят сообщения на экран "move" и "stop",
а birthday увеличивает атрибут age на 1. Атрибут brand, age, mark являются обязательными при объявлении объекта.'''


class Auto:
    def __init__(self, brand: str, age: int, mark: str, color: str = "", weight: float = 0.0):
        self.brand = brand
        self.age = age
        self.mark = mark
        self.color = color
        self.weight = weight

    def move(self):
        print("move")

    def birthday(self):
        self.age += 1

    def stop(self):
        print("stop")


car1 = Auto(brand="Dodge", age=3, mark="Challenger", color="Black", weight=1750)
car2 = Auto(brand="Nissan", age=20, mark="Primera")
car3 = Auto(brand="Lada", age=50, mark="2101", color="Yellow")

car1.move()  # Выводит "move"
print(car1.mark)  # Выводит Challenger
print(car1.age)  # Выводит 3
car1.birthday()
print(car1.age)  # Выводит 4
car1.stop()  # Выводит "stop"

print()

car2.move()  # Выводит "move"
print(car2.brand, car2.mark)  # Выводит Nissan Primera
print(car2.age)  # Выводит 3
car2.birthday()
print(car2.age)  # Выводит 21
car2.stop()  # Выводит "stop"
