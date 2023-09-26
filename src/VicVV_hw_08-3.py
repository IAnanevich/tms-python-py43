# Создать 2 класса truk и car из auto
import time


class Auto:
    def __init__(self, brand, age: int, mark, color_=None, weight=0):
        self.brand = brand
        self.age = age
        self.mark = mark
        self.color_ = color_
        self.weight = weight

    @staticmethod
    def move():
        print("I'm move")

    def birthday(self):
        self.age = int(self.age) + 1
        return self.age

    @staticmethod
    def stop():
        print("I'm stop")

    def __str__(self):
        str_ = (
            f"I'm {self.brand} {self.mark}, my color is {self.color_}."
            f"I'm from {self.age} and my weight is {self.weight}"
        )
        return str_


class Truk(Auto):
    def __init__(self, max_load, brand, age: int, mark, color_=None, weight=0):
        Auto.__init__(self, brand, age, mark, color_, weight)
        self.max_load = max_load

    def move(self):
        print("attention!")
        super().move()

    @staticmethod
    def load():
        time.sleep(1)
        print("I'm load")
        time.sleep(1)


class Car(Auto):
    def __init__(self, max_sped, brand, age: int, mark, color_=None, weight=0):
        Auto.__init__(self, brand, age, mark, color_, weight)
        self.max_sped = max_sped

    def move(self):
        print("I'm move")
        print(f"max sped is {self.max_sped}")


my_Truk = Truk(brand="Honda", age=2000, mark="Pilot", color_="Silver", weight=2500, max_load=3000)
my_Truk.load()
my_Truk.move()
print(f"I'm from {my_Truk.birthday()}")
my_Truk.stop()
print(my_Truk)
print("===============================================")
my_car = Car(brand="Honda", age=2000, mark="Civic", color_="Silver", weight=1200, max_sped=180)
my_car.move()
print(f"I'm from {my_car.birthday()}")
my_car.stop()
print(my_car)
