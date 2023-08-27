# Создать родительский класс auto, у которого есть атрибуты: brand, age, color, mark
# и weight. А так же методы: move, birthday и stop. Методы "move" и "stop" выводят
# сообщение на экран "move" и "stop", а birthday увеличивает атрибут age на 1.
# Атрибуты brand, age и mark являются обязательными при объявлении объекта.

class Auto:
    def __init__(self, brand: str, age: int, color: str, mark: str, weight: int):
        self.brand = brand
        self.age = age
        self.color = color
        self.mark = mark
        self.weight = weight

    def move(self):
        print('move')

    def stop(self):
        print('stop')

    def berthday(self):
        self.age += 1


car = Auto(brand='BMW', age=2, color='black', mark='m340i', weight=1710)
car.move()
car.stop()
car.berthday()
print(f'the car is already {car.age} years old')
