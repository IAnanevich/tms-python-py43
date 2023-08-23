# Создать 2 класса truck и car, которые является наследниками класса auto. Класс
# truck имеет дополнительный обязательный атрибут max_load. Переопределенный
# метод move, перед появлением надписи "move" выводит надпись "attention", его
# реализацию сделать при помощи оператора super. А так же дополнительный метод
# load. При его вызове происходит пауза 1 сек., затем выдаётся сообщение "load" и
# снова пауза 1 сек. Класс car имеет дополнительный обязательный атрибут
# max_speed и при вызове метода move, после появления надписи "move" должна
# появиться надпись "max_speed is <max_speed>". Создать по 2 объекта для каждого
# из классов truck car, проверить все их методы и атрибуты.
from andrey_hw8_2 import Auto
import time


class Truck(Auto):
    def __init__(self, max_load, brand: str, age: int, mark: str, color: str = '', weight: int = 0):
        Auto.__init__(self, brand, age, mark, color, weight)
        self.max_load = max_load

    def move(self):
        print("attention")
        super().move()

    @staticmethod
    def load():
        time.sleep(1)
        print("load")
        time.sleep(1)


class Car(Auto):
    def __init__(self, max_speed, brand: str, age: int, mark: str, color: str = '', weight: int = 0):
        Auto.__init__(self, brand, age, mark, color, weight)
        self.max_speed = max_speed

    def move(self):
        super().move()
        print(f"max_speed is {self.max_speed}")


if __name__ == "__main__":
    obj_Truck1 = Truck(7100, "DAF", 7, "XF", 'white')
    obj_Truck2 = Truck(9000, "Scania", 12, "P360", weight=7485)
    obj_Car1 = Car(186, "Lada", 4, "Vesta", "gray")
    obj_Car2 = Car(175, "Dacia", 1, "Logan", weight=2409)
    obj_Truck1.move()
    obj_Truck1.stop()
    obj_Truck2.load()
    print(f"age: {obj_Truck2.age}")
    obj_Truck2.birthday()
    print(f"age: {obj_Truck2.age}")
    obj_Car1.move()
    obj_Car1.stop()
    obj_Car2.move()
    print(f"age: {obj_Car2.age}")
    obj_Car2.birthday()
    print(f"age: {obj_Car2.age}")
