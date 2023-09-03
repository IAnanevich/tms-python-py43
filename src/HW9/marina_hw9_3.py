# Реализовать датакласс и использовать его как объект в конструкторе для задания ниже:
# Реализовать любой класс на свой выбор. В нем сделать:
# конструктор, несколько методов (один обязательно static, один class, один обычный),
# переопределить один любой из магических методов (__lt__ и тд), сделать один метод protected.
# Сделать проверку, что все работает (создать объекты от классов).

from accessify import protected
from dataclasses import dataclass
from typing_extensions import Any


@dataclass
class Person:
    """
    information about person Name, Last_name and age
    """

    name: str
    last_name: str
    age: int


class Department:
    """
    description employees of department
    """

    def __init__(
        self, name: Person, age: Person, position: str, experience: int
    ) -> None:
        """
        initialize attributes of class object
        :param name: employee's name
        :param age: employee's age
        :param position: employee's job title
        :param experience: number of years of work
        """
        self.name = f"{name.name} {name.last_name}"
        self.age = age.age
        self.position = position
        self.experience = experience

    @staticmethod
    def welcome() -> None:
        """
        print Welcome string
        :return: None
        """
        print("Hello my friend")

    @classmethod
    def name_of_class(cls) -> None:
        """
        print name of Class
        :return: None
        """
        print(cls.__name__)

    def employees_info(self) -> None:
        """
        display info Name and Position in Department
        :return: None
        """
        self.get_info()

    # переопределим ">"
    def __gt__(self, other: Any) -> bool:
        """
        checking if the first person works more than the second
        :param other: person who with we compare experience
        :return: result of check
        """
        return self.experience > other.experience

    @protected
    def get_info(self) -> None:
        """
        display sentence name and position in company with correct article
        :return: None
        """
        # if position starts with vowel - use "an"
        if self.position[0] in "aeiouy":
            print(f"{self.name} is an {self.position}")
        else:
            print(f"{self.name} is a {self.position}")


# класс Department
pers_1 = Person(name="Marina", last_name="Pudova", age=33)
pers_2 = Person(name="Petr", last_name="Petrov", age=40)
person_1 = Department(name=pers_1, age=pers_1, position="analyst", experience=6)
person_2 = Department(name=pers_2, age=pers_2, position="specialist", experience=13)
# проверяем класс-метод
print("! Check class method:")
person_1.name_of_class()
# выводим инфо по объектам класса Department
print("! Objects in Department:")
print(person_1.__dict__, person_2.__dict__, sep="\n")
# проверяем статик-метод
print("! Check staticmethod:")
person_1.welcome()
# проверяем обычный метод, который использует протектед-метод
print("! Check ordinary method:")
person_1.employees_info()
person_2.employees_info()
# проверка переопределенного оператора ">"
print(f"! Check '>':\n {person_1.name} > {person_2.name} is {person_1 > person_2}\n")
