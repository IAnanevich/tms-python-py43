"""
Создать 2 класса truck и car, которые является наследниками класса auto. Класс
truck имеет дополнительный обязательный атрибут max_load. Переопределенный
метод move, перед появлением надписи "move" выводит надпись "attention", его
реализацию сделать при помощи оператора super. А так же дополнительный метод
load. При его вызове происходит пауза 1 сек., затем выдаётся сообщение "load" и
снова пауза 1 сек. Класс car имеет дополнительный обязательный атрибут
max_speed и при вызове метода move, после появления надписи "move" должна
появиться надпись "max_speed is <max_speed>". Создать по 2 объекта для каждого
из классов truck car, проверить все их методы и атрибуты.
"""
from oleg_hw8_2 import Auto
import time


class Truck(Auto):
    def __init__(self, max_load: int, brand: str, age: int, mark: str, color: str = '', weight: int = 0):
        super().__init__(brand, age, mark, color, weight)
        self.max_load = max_load

    def move(self) -> None:
        """ print 'attention' and call parent move() """
        print("attention")
        super().move()

    def load(self) -> None:
        """ delay 1s -> print 'load' -> delay 1s """
        time.sleep(1)
        print("load")
        time.sleep(1)


class Car(Auto):
    def __init__(self, max_speed: int, brand: str, age: int, mark: str, color: str = '', weight: int = 0):
        super().__init__(brand, age, mark, color, weight)
        self.max_speed = max_speed

    def move(self) -> None:
        """ call parent move() print 'max_speed' """
        super().move()
        print(f"max_speed is {self.max_speed}")

if __name__ == "__main__":
    truck_1 = Truck(max_load=9700, brand="МАЗ", age=5, mark="53363", color='white', weight=8300)
    truck_2 = Truck(max_load=20000, brand="КамАЗ", age=14, mark="5320", color='black', weight=7000)
    car_1 = Car(max_speed=240, brand="Citroen", age=11, mark="C5", color="gray")
    car_2 = Car(max_speed=220, brand="Toyota", age=17, mark="Avensis", color="blue")

    truck_1.move()
    truck_1.load()
    truck_1.stop()
    print(f"Age '{truck_1.brand} - {truck_1.mark}' - {truck_1.age}")
    truck_1.birthday()
    print(f"Age '{truck_1.brand} - {truck_1.mark}' after party - {truck_1.age}")
    truck_2.move()

    car_1.move()
    car_1.stop()
    print(f"Age '{car_1.brand} - {car_1.mark}' - {car_1.age}")
    car_1.birthday()
    print(f"Age '{car_1.brand} - {car_1.mark}' after party - {car_1.age}")
    car_2.move()