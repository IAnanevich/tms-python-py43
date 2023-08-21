# Создать родительский класс Auto, у которого есть Атрибуты: brand, age, color, mark, weight.
# Методы move, bithday, stop.
# Методы  "move" и "stop" выводят сообщения на экран "move" и "stop", а birthday увеличивает атрибут age на 1.
# Атрибуты brand, age и mark обязательные при объявлении объекта.
class Auto:
    def __init__(self, brand: str, age: int, mark: str, color: str = "", weight: float = 0):
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


car_one = Auto("mazda", 7, "ford")
car_one.move()
car_one.stop()
car_one.birthday()

print(car_one.brand, car_one.age, car_one.color, car_one.mark, car_one.weight)
