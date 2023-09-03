from datetime import datetime


class Item:
    """Базовый класс для всех предметов"""
    count_items = 0 # количество заведенных предметов в рамках подкласса

    def __init__(self, name: str, width: float, height: float, weight: float):
        self.name = name
        self.width = width
        self.height = height
        self.weight = weight
        self.counter(self)

    @classmethod
    def counter(cls, self) -> None:
        """ можно конечно было бы просто в init подсчитывать, но просто ради метода вынес сюда """
        self.__class__.count_items += 1

    @staticmethod
    def isAdult(age, min_age):
        return age >= min_age

    def __del__(self):
        str_log = str(datetime.now())
        for key, value in vars(self).items():
            str_log += f" {key} = {value},"

        with open("log_file_hw9.txt", "a+") as text_file:
            text_file.write(f"{str_log}\r")


class Toy(Item):
    """class Toy (Игрушка)."""
    child_age = 0 # возраст ребенка который будет играть с этой игрушкой

    def __init__(self, name: str, width: float, height: float, weight: float, minimum_age: int, num_battery: int = 0):
        super().__init__(name, width, height, weight)
        self.minimum_age = minimum_age # минимальный возраст
        self.num_battery = num_battery # количество бареек

    def canPlay(self):
        return f"Ребенок может играть с '{self.name}'" if self.__access() else f"Ребенок запрещено играть с '{self.name}''. Минимальный возраст {self.minimum_age}"

    def __access(self) -> bool:
        return self.child_age >= self.minimum_age


class BuildingTools(Item):
    """class BuildingTools (Строительный инструмент)."""
    def __init__(self, name: str, width: float, height: float, weight: float, type: str = "mechanical", only_socket = False, num_battery: int = 0):
        super().__init__(name, width, height, weight)
        self.type = type # тип инструмента
        self.num_battery = num_battery # количество батареек
        self.only_socket = only_socket # только от розетки

toy_1 = Toy(name="Машинка электрическая", width=10, height=15, weight=75, minimum_age=3, num_battery=5)
toy_1.child_age = 2
print(toy_1.canPlay())
print(Toy.isAdult(10, 9))

toy_2 = Toy(name="Плюшевый мишка", width=50, height=100, weight=50, minimum_age=1)
toy_2.child_age = 2
print(toy_2.canPlay())

b_tools_1 = BuildingTools(name="Шлифовальная машина", width=50, height=40, weight=600, type="electric", num_battery=1)
b_tools_2 = BuildingTools(name="Молоток", width=10, height=30, weight=150, type="mechanical")

print(f"Кол-во заведенных игрушек {toy_1.count_items}");
print(f"Кол-во заведенных инструментов {b_tools_2.count_items}");
del b_tools_1, b_tools_2, toy_1, toy_2
