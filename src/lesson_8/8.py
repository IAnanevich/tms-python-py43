# # from abc import ABC, abstractmethod
# #
# #
# # class Person:
# #     # name = 'Tom'
# #
# #     def __init__(self, name: str, age: int, is_head:  bool | None = True):
# #         self.name = name
# #         self.age = age
# #         self.is_head = is_head
# #
# #     def my_age(self):
# #         print(f'My age is {self.age}')
# #
# #     def my_name(self, name='Petr') -> None:
# #         # print(self)
# #         # print(self.my_age())
# #         print(f'Hello, my name {self.name}')
# #         print(self._info())
# #         # print(self.__secret_info())
# #
# #     def _info(self):
# #         return 'Some info about me'
# #
# #     def __secret_info(self):
# #         return 'Some secret info about me'
# #
# #
# # class Child(Person):
# #
# #     # def __init__(self):
# #     #     pass
# #
# #     def say(self):
# #         print('Hello world')
# #
# #     def my_age(self):
# #         print(f'My age is {self.age}. I am < 18')
# #
# #
# # # child_1 = Child('Pavel', 10)
# # # print(dir(child_1))
# # # child_1.my_name()
# # # child_1.say()
# # # child_1.my_age()
# #
# # # person_1 = Person(name='Tom', age=20, is_head=True)
# # # person_1.my_name(name='Tom')
# # # person_1.my_age()
# # # person_1.say()
# # # # print(person_1._info())
# # # # print(person_1.__secret_info())
# # # # print(person_1._Person__secret_info())
# # #
# # # print()
# # #
# # # # Person().my_name()
# # #
# # # person_2 = Person(name='Alex', age=25)
# # # # print(person_2)
# # # person_2.my_name(name='Alex')
# # # person_2.my_age()
# #
# #
# # class Animal(ABC):
# #
# #     def move(self):
# #         print('Move')
# #
# #     @abstractmethod
# #     def make_sound(self):
# #         pass
# #
# #
# # class Cat(Animal):
# #
# #     def make_sound(self):
# #         print('Meow')
# #
# #
# # class Dog(Animal):
# #
# #     def make_sound(self):
# #         print('Wow')
# #
# #     def security(self):
# #         pass
# #
# #
# # # dog = Dog()
# # # cat = Cat()
# # # dog.make_sound()
# # # dog.move()
# # # cat.make_sound()
# #
# # # animal = Animal()
# # # animal.move()
# #
# # # Animal().move()
# #
# #
# # class A:
# #     def say(self):
# #         print('A')
# #
# #
# # class B(A):
# #     def say(self):
# #         print('B')
# #     # pass
# #
# #
# # class C(A):
# #     def say(self):
# #         print('C')
# #
# #
# # class D(C, B):
# #     def say(self):
# #         print('D')
# #     # pass
# #
# #
# # d = D()
# # d.say()
# # # print(D.mro())
# #
#
#
# # class Person:
# #
# #     def __init__(self, age: int):
# #         self.age = age
# #
# #     def __add__(self, other):
# #         return self.age + other.age
# #
# #     def __sub__(self, other):
# #         return self.age - other.age
# #
# #     def __repr__(self):
# #         return str(self.age)
# #
# #
# # person_1 = Person(age=10)
# # person_2 = Person(age=20)
# # person_3 = Person(age=30)
# # print(person_1 + person_2)
# # print(person_3 - person_1)
# # print(person_1)
#
#
# class Point:
#
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def calc(self):
#         return (self.x ** 2 + self.y ** 2) ** 0.5
#
#     def __ge__(self, other):
#         return self.calc() > other.calc()
#
#     def __add__(self, other):
#         return Point(self.x + other.x, self.y + other.y)
#
#
# point_1 = Point(10, 10)
# point_2 = Point(15, 7)
# point_3 = Point(25, 17)
# print(point_2 >= point_1)
# point_3 = point_1 + point_2 + point_3
# print(point_3.x, point_3.y)

