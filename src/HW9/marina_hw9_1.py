# Реализовать любой класс на свой выбор. В нем сделать:
# конструктор, несколько методов (один обязательно static, один class, один обычный),
# переопределить один любой из магических методов (__lt__ и тд), сделать один метод protected.
# Сделать два класса дочерних. В этих классах переопределить все методы и конструктор,
# которые можете (один метод должен быть переопределен ТОЛЬКО ОДИН раз в любом классе ребенке)
# Сделать проверку, что все работает (создать объекты от классов).
from accessify import protected


class Department:
    """
    description employees of department
    """

    def __init__(self, name: str, age: int, position: str, experience: int) -> None:
        """
        initialize attributes of class object
        :param name: employee's name
        :param age: employee's age
        :param position: employee's job title
        :param experience: number of years of work
        """
        self.name = name
        self.age = age
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
    def __gt__(self, other: object) -> bool:
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


# ------------------------------------------------------------------------------------
# первый дочерний класс
class Sales(Department):
    """
    people who work for sales department
    """

    def __init__(
        self, name: str, age: int, position: str, experience: int, numb_of_sub: int
    ) -> None:
        """
        initialize attributes of class object
        :param name: employee's name
        :param age: employee's age
        :param position: employee's job title
        :param experience: number of years of work
        :param numb_of_sub: number of subordinates
        """
        super().__init__(name, age, position, experience)
        self.numb_of_sub = numb_of_sub

    # переопределяем метод родительского класса Department
    @staticmethod
    def welcome() -> None:
        """
        print Welcome string
        :return: None
        """
        print("Welcome to the Sales department")

    # @classmethod
    # def name_of_class(cls) -> None:
    #     """
    #     print name of Class
    #     :return: None
    #     """
    #     super().name_of_class()

    def employees_info(self) -> None:
        """
        display info Name and Position in Department
        :return: None
        """
        self.get_info()

    # переопределим ">" для дочернего класса
    def __gt__(self, other: object) -> bool:
        """
        checking if the first person has more subordinates than the second
        :param other: person who with we compare number of sub
        :return: result of check
        """
        return self.numb_of_sub > other.numb_of_sub

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


# ------------------------------------------------------------------------------------
# второй дочерний класс
class Merch(Department):
    """
    people who work for merch department
    """

    def __init__(
        self, name: str, age: int, position: str, experience: int, numb_of_stores: int
    ) -> None:
        """
        initialize attributes of class object
        :param name: employee's name
        :param age: employee's age
        :param position: employee's job title
        :param experience: number of years of work
        :param numb_of_stores: number of stores where merch works
        """
        super().__init__(name, age, position, experience)
        self.numb_of_stores = numb_of_stores

    # @staticmethod
    # def welcome() -> None:
    #     """
    #     print Welcome string
    #     :return: None
    #     """
    #     print("Hello my friend")

    # переопределяем класс-метод
    @classmethod
    def name_of_class(cls) -> None:
        """
        print description of class
        :return: None
        """
        print(cls.__doc__)

    # переопределим
    def employees_info(self) -> None:
        """
        display Attention and after that info Name and Position in Department
        :return: None
        """
        print("Attention")
        self.get_info()

    # # переопределим ">"
    # def __gt__(self, other) -> bool:
    #     """
    #     checking if the first person works more than the second
    #     :param other: person who with we compare experience
    #     :return: result of check
    #     """
    #     return self.experience > other.experience

    # переопределим
    @protected
    def get_info(self) -> None:
        """
        display sentence name and number of stores
        :return: None
        """
        print(f"{self.name} has {self.numb_of_stores} stores")


# класс Department
person_1 = Department(name="Marina Pudova", age=33, position="analyst", experience=6)
person_2 = Department(name="Petr Petrov", age=40, position="specialist", experience=13)
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
#
# класс Sales
sales_1 = Sales(
    name="Alla Pugach", age=43, position="manager", experience=10, numb_of_sub=4
)
sales_2 = Sales(
    name="Petr Petrov", age=25, position="specialist", experience=3, numb_of_sub=0
)
# проверяем класс-метод
print("! Check class method:")
sales_1.name_of_class()
# выводим инфо по объектам класса Department
print("! Objects in Sales:")
print(sales_1.__dict__, sales_2.__dict__, sep="\n")
# проверяем статик-метод
print("! Check staticmethod:")
sales_1.welcome()
# проверяем обычный метод, который использует протектед-метод
print("! Check ordinary method:")
sales_1.employees_info()
sales_2.employees_info()
# проверка переопределенного оператора ">"
print(f"! Check '>':\n {sales_1.name} > {sales_2.name} is {sales_1 > sales_2}\n")
#
# класс Merch
merch_1 = Merch(
    name="Oleg Malakhov", age=18, position="merch", experience=1, numb_of_stores=56
)
merch_2 = Merch(
    name="Fedor Ivanov", age=23, position="merch", experience=3, numb_of_stores=82
)
# проверяем класс-метод
print("! Check class method:")
merch_1.name_of_class()
# выводим инфо по объектам класса Department
print("! Objects in Merch:")
print(merch_1.__dict__, merch_2.__dict__, sep="\n")
# проверяем статик-метод
print("! Check staticmethod:")
merch_1.welcome()
# проверяем обычный метод, который использует протектед-метод
print("! Check ordinary method:")
merch_1.employees_info()
merch_2.employees_info()
# проверка переопределенного оператора ">"
print(f"! Check '>':\n {merch_1.name} > {merch_2.name} is {merch_1 > merch_2}\n")
