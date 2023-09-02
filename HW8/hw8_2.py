# Создать родительский класс Auto, у которого есть
# Атрибуты: brand, age, color, mark, weight.
# Методы move, bithday, stop.
# Методы  move и stop выводят сообщения на экран "move" и "stop", а birthday увеличивает атрибут age на 1.
# Атрибуты brand, age и mark обязательные при объявлении объекта.
class Auto:
    def __init__(self, brand: str, age: int, mark: str, color: str = "no color", weight: float = 0) -> None:
        # Инициализация класса по параметрам
        self.brand = brand
        self.age = age
        self.color = color
        self.mark = mark
        self.weight = weight

    @staticmethod
    def move() -> None:
        """
        Движемся
        :return: Ничего
        """
        print("move")

    @staticmethod
    def stop() -> None:
        """
        Стоим
        :return: Ничего
        """
        print("stop")

    def birthday(self) -> None:
        """
        Увеличиваем возраст на 1
        :return: Ничего
        """
        self.age += 1


my_auto = Auto(brand="some brand", age=3, mark="some mark")
my_auto.move()
my_auto.stop()
my_auto.birthday()

print(my_auto.brand, my_auto.age, my_auto.mark, my_auto.color, my_auto.weight)
