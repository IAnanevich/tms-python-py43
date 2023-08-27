# Создать 2 класса truck и car, которые является наследниками класса auto. Класс
# truck имеет дополнительный обязательный атрибут max_load. Переопределенный
# метод move, перед появлением надписи "move" выводит надпись "attention", его
# реализацию сделать при помощи оператора super. А так же дополнительный метод
# load. При его вызове происходит пауза 1 сек., затем выдаётся сообщение "load" и
# снова пауза 1 сек. Класс car имеет дополнительный обязательный атрибут
# max_speed и при вызове метода move, после появления надписи "move" должна
# появиться надпись "max_speed is <max_speed>". Создать по 2 объекта для каждого
# из классов truck car, проверить все их методы и атрибуты.

import time


class Auto():
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


class Truck(Auto):
    def __init__(self, brand: str, age: int, color: str, mark: str, weight: int, max_load: int):
        super().__init__(brand, age, color, mark, weight)
        self.max_load = max_load

    def move(self):
        print('attention')
        super().move()

    def stop(self):
        print('stop')

    def birthday(self):
        self.age += 1

    def load(self):
        time.sleep(1)
        print('load')
        time.sleep(1)


class Car(Auto):
    def __init__(self, brand: str, age: int, color: str, mark: str, weight: int, max_speed: int):
        super().__init__(brand, age, color, mark, weight)
        self.max_speed = max_speed

    def move(self):
        print(f'max speed is {self.max_speed}')

    def stop(self):
        print('stop')

    def birthday(self):
        self.age += 1


car_1 = Car(brand='BMW', age=2, color='black', mark='m340i', weight=1710, max_speed=276)
car_2 = Car(brand='Nissan', age=21, color='blue', mark='gt-r34', weight=1550, max_speed=250)

truck_1 = Truck(brand='MAN', age=11, color='white', mark='TGS', weight=7300, max_load=18000)
truck_2 = Truck(brand='Volvo', age=5, color='green', mark='FH', weight=8100, max_load=22000)

car_1.move()
car_1.stop()
car_1.birthday()
print(f'brand {car_1.brand}')
print(f'age {car_2.age}')
print('___________')
truck_1.move()
truck_1.stop()
truck_1.birthday()
print(f'max load is {truck_2.max_load}')
truck_1.load()
print(f'age is {truck_2.age}')
