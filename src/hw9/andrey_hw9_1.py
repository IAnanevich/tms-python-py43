# 1) Реализовать любой класс на свой выбор. В нем сделать:
# конструктор
# несколько методов (один обязательно статикметод, один классметод, один обычный)
# переопределить один любой из магических методов (__lt__ и тд)
# сделать один метод протектед.
#
# Сделать два класса дочерних. В этих классах переопределить все методы и конструктор,
# которые можете (один метод должен быть переопределен ТОЛЬКО ОДИН раз в любом классе ребенке)
#
# Сделать проверку, что все работает (создать обьекты от классов)

class Animal:
    """
    describes the animal
    """

    def __init__(self, name: str, age: int) -> None:
        from random import randint
        self.name = name
        self.age = age
        self.lifespan = age + randint(0, 500)

    def __lt__(self, other: object) -> bool | None:
        if not isinstance(self, Animal):
            return
        return self.age < other.age

    @staticmethod
    def movement() -> str:
        """
        what they use to move
        :return:
        """
        return 'different'

    @classmethod
    def info(cls) -> str | None:
        """
        class information
        :return:
        """
        return cls.__doc__

    @property
    def points(self) -> int:
        """
                rest of life
                :return:
                """
        return self.lifespan - self.age


class Mammals(Animal):
    """
       describes the Mammals
    """

    @classmethod
    def info(cls) -> str:
        """
        class information
        :return:
        """
        return f'{cls}: {cls.__doc__}'


class Fish(Animal):
    """
    describes the Fish
    """

    def __init__(self, name: str, age: int, size: float) -> None:
        super().__init__(name, age)
        from random import randint
        self.lifespan = age + randint(0, 300)
        self.size = size

    @staticmethod
    def movement() -> str:
        """
        what they use to move
        :return:
        """
        return 'flippers'

    @property
    def points(self) -> float:
        """
        rest of life
        :return:
        """
        coef = 0.1
        if self.size <= 10:
            coef = 0.9
        if self.size <= 30:
            coef = 0.5
        if self.size <= 50:
            coef = 0.3

        return (self.lifespan - self.age) * coef

    def __lt__(self, other: object) -> bool | None:
        if not isinstance(other, Fish):
            return
        return self.size < other.size


if __name__ == "__main__":
    animal = Animal(name='animal', age=13)
    animal_2 = Animal(name='animal', age=3)
    print(animal.info())
    print(animal.movement())
    print(animal.points)
    print(animal < animal_2)
    print('-' * 20)

    human = Mammals(name='Human', age=50)
    cow = Mammals(name='cow', age=2)
    print(human.info())
    print(human.movement())
    print(human.points)
    print(human < cow)
    print('-' * 20)

    trout = Fish(name='trout', age=12, size=1)
    tuna = Fish(name='tuna', age=1, size=10)
    print(trout.info())
    print(trout.movement())
    print(trout.points)
    print(trout < tuna)
    print('-' * 20)
