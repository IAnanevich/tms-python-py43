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


class Auto:
    def __init__(self,
                 brand: str,
                 age: int,
                 mark: str,
                 color: str = "",
                 weight: float = 0
                 ):
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


class Truck(Auto):
    def __init__(self,
                 brand: str,
                 age: int,
                 mark: str,
                 color: str,
                 weight: int,
                 max_load: int
                 ):
        Auto.__init__(self, brand, age, mark, color, weight)
        self.max_load = max_load

    def move(self):
        print("attention")
        super().move()

    @staticmethod
    def load():
        import time
        time.sleep(1)
        print('Loading')
        time.sleep(1)


class Car(Auto):
    def __init__(self,
                 brand=str,
                 age=int,
                 mark=str,
                 color=str,
                 weight=int,
                 max_speed=int,
                 ):
        Auto.__init__(self, brand, age, mark, color, weight)
        self.max_load = max_speed()

    def move(self):
        max_speed = int()
        super().move()
        print(f"Max speed  {max_speed}")


car_one = Car("mazda", 9, "UNO")
car_one.move()
car_one.birthday()
car_one.stop()
