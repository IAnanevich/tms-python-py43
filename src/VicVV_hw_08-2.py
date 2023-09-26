# Создать класс auto


class Auto:
    def __init__(self, brand, age: int, mark, color_=None, weight=0):
        self.brand = brand
        self.age = age
        self.mark = mark
        self.color_ = color_
        self.weight = weight

    @staticmethod
    def move():
        print(f"I'm move")

    def birthday(self):
        self.age = int(self.age) + 1
        return self.age

    @staticmethod
    def stop():
        print(f"I'm stop")

    def __str__(self):
        print(
            f"I'm {self.brand} {self.mark}, my color is {self.color_}. "
            f"I'm from {self.age} and my weight is {self.weight}"
        )


my_car = Auto(brand="Honda", age=2000, mark="Civic", color_="Silver", weight=1200)
my_car.move()
print(f"I'm from {my_car.birthday()}")
my_car.stop()
