from time import sleep

# Создать родительский класс auto, у которого есть
# атрибуты brand, age, color, mark и  weight.
# а также методы move, bithday и stop.
# методы  move и strstop выводят сообщения на экран
# "move" и "stop", а birthday увеличивает атрибут age на 1.
# Атрибуты brand, age и mark обязательные при объявлении объекта.


class Auto:
    def __init__(self, brand: str, age: int, mark: str, color: str = " ", weight: int = 0):
        self.brand = brand
        self.age = age
        self.mark = mark
        self.color = color
        self.weight = weight

    @staticmethod
    def move():
        print("move")

    def birthday(self):
        self.age += 1
        print(self.age)

    @staticmethod
    def stop():
        print("stop")


auto_1 = Auto("ford", 6, "777")
auto_1.move()
auto_1.stop()
auto_1.birthday()


# создать два класса, которые являются наследниками класса auto.
# класс truck имеет дополнительный обязательный атрибут max_load,
# переопределенный  метод move  и дополнительный метод load.
# При его вызове происходит пайза в 1 сек, затем выдвет сообщение load,
# и снова пауза в 1 секунду. класс car имеет дополнительный обязательны
# атрибут max_speed  и при вызове метода move,  после появления надписи move
# должна появиться запись 'max speed is {max_speed}' создать по 2 объекта


class Truck(Auto):
    def __init__(self, brand: str, age: int, mark: str, color: str, weight: int, max_load: int):
        Auto.__init__(self, brand, age, mark, color, weight)
        self.max_load = max_load

    def move(self):
        print("attention")
        super().move()

    @staticmethod
    def load(self):
        sleep(1)
        print("'LOAD'")
        sleep(1)


class Car(Auto):
    def __init__(
        self,
        max_speed=int,
        brand=str,
        age=int,
        mark=str,
        color=str,
        weight=int,
    ):
        Auto.__init__(self, brand, age, mark, color, weight)
        self.max_load = max_speed

    def move(self, max_speed=int):
        super().move()
        print(f"max speed is {max_speed}")


car_1 = Car(300, "bmw", 9, "7")
car_1.move(300)
car_1.birthday()
car_1.stop()
