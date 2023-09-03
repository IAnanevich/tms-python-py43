# Создать 2 класса truck и car, которые является наследниками класса auto. Класс
# truck имеет дополнительный обязательный атрибут max_load. Переопределенный
# метод move, перед появлением надписи "move" выводит надпись "attention", его
# реализацию сделать при помощи оператора super. А так же дополнительный метод
# load. При его вызове происходит пауза 1 сек., затем выдаётся сообщение "load" и
# снова пауза 1 сек. Класс car имеет дополнительный обязательный атрибут
# max_speed и при вызове метода move, после появления надписи "move" должна
# появиться надпись "max_speed is <max_speed>". Создать по 2 объекта для каждого
# из классов truck  car, проверить все их методы и атрибуты.
from maxim_hw8_2 import Auto
from time import sleep


class Truck(Auto):

    def __init__(self,
                 brand: str,
                 age: int,
                 mark: str,
                 max_load: int | float,
                 color: str = "",
                 weight: int | float = 0):
        super().__init__(brand, age, mark, color, weight)
        self.max_load = max_load

    def move(self):
        print("attention")
        super().move()

    @staticmethod
    def load():
        sleep(1)
        print("load")
        sleep(1)


class Car(Auto):

    def __init__(self, brand: str, age: int, mark: str, max_speed: int, color: str = "", weight: int | float = 0):
        super().__init__(brand, age, mark, color, weight)
        self.max_speed = max_speed

    def move(self):
        super().move()
        print(f"max_speed is {self.max_speed}")


if __name__ == "__main__":
    obj_Truck1 = Truck("DAF", 7, "XF", 7100, "white")
    obj_Truck2 = Truck("Scania", 12, "P360", 9000, weight=7485)
    obj_Car1 = Car("Lada", 4, "Vesta", 186, "gray")
    obj_Car2 = Car("Dacia", 1, "Logan", 175, weight=2409)
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
