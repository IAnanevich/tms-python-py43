import pdb
import os

# for i in range(10):
#     print(i)

# iterator has __iter__(), __next__()
# генератор = итератор (любой генератор это итератор)
# итератор != генератор (не каждый итератор является генератором)


# class Counter:
#     def __init__(self, low, high):
#         self.current = low - 1
#         self.high = high
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         self.current += 1
#         if self.current < self.high:
#             return self.current
#         raise StopIteration
#
#
# for i in Counter(3, 10):
#     print(i)


# 1 1 2 3 5 8 13 21 34 ...


# class FibonacciIterator:
#     def __init__(self, limit: int):
#         self.limit = limit
#         self.a, self.b = 1, 1
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if not self.limit:
#             raise StopIteration
#         result = self.a
#         self.a, self.b = self.b, self.a + self.b
#         self.limit -= 1
#         return result


# for i in [0, 1, 2]:
#     pass
    # 1: i = 0
    # 2: i = 1
    # 3: i = 2


# for index, number in enumerate(FibonacciIterator(100)):
#     print(f'{index}: {number}')
    # 1: number = FibonacciIterator(100)
    # 2: number = FibonacciIterator(99)
    # 3: number = FibonacciIterator(98)


# def fibonacci():
#     prev, cur = 1, 1
#     while True:
#         yield prev
#         prev, cur = cur, prev + cur
#
#
# for i in fibonacci():
#     print(i)
#     if i > 100:
#         break
#
#
#         return [1, 2, 3]
#     yield i # in [1, 2, 3]

#
# def main():
#     for i in range(10):
#         yield i
#
#
# res = main()
# for _ in range(10):
#     print(next(res))
#
#
# a = [1, 2, 3]
# itrator = iter(a)


# for i in range(10):
#     print(i)
#     print('hello')


# def main():
#     a = []
#     for i in range(10):
#         a.append(i)
#     return a
#
#
# print('hello')
# print(main())


# print(os.getenv('DB_USER'))
# print(os.environ['DB_USER'])


# import re
#
# text = 'Hellow world, my email is test@gmail.com, test1@gmail.com'
# pattern = r'\S+@\S+'
#
# res = re.search(pattern=pattern, string=text)
# print(res.group())
#
# res = re.match(pattern=pattern, string=text)
# print(res)
#
# res = re.fullmatch(pattern=pattern, string=text)
# print(res)
#
# res = re.findall(pattern=pattern, string=text)
# print(res)
#
# res = re.finditer(pattern=pattern, string=text)
# print(res)
# for i in res:
#     print(i.group())
#
#
# text = "Hello, world! How are you?"
# pattern = r'world'
# replacement = 'Python'
# new_text = re.sub(pattern, replacement, text)
# print("Замененный текст:", new_text)
#
#
# pattern = re.compile(r'\d{2}-\d{2}-\d{4}')
# text = "Дата начала проекта: 05-09-2023, дата окончания: 10-10-2023"
# matches = pattern.findall(text)
# print("Список совпадений:", matches)


# SOLID
# S - Это означает, что класс должен иметь только одну ответственность.
# Пример: Рассмотрим класс `User`, который отвечает и за аутентификацию пользователя, и за отправку уведомлений.
# Этот класс нарушает SRP. Более правильно было бы создать отдельные классы для аутентификации и уведомлений.
# Принцип единственной ответственности (Single Responsibility Principle - SRP)


class User:
    pass


class UserActionOnSite(User):
    def sign_up(self):
        pass

    def login(self):
        pass


class UserPushNotification(User):
    def push(self):
        pass


# class UserCompany(User):
#     def create_company(self):
#         pass

# O - Программные сущности (классы, модули, функции и т.д.) должны быть открыты для расширения, но закрыты для изменения
# Новая функциональность должна добавляться путем расширения существующего кода, а не его модификации.
# - Принцип открытости/закрытости (Open/Closed Principle, OCP):


class UserCompany(User):
    def _add_info(self):
        pass

    def create_company(self):
        pass

    def update_company(self):
        self._add_info()

# L - Объекты базового класса должны быть заменяемыми объектами его производных классов без изменения
# правильности выполнения программы.
# Если у вас есть базовый класс Bird и производный класс Penguin, то код, который работает с объектами типа Bird,
# должен также работать и с объектами типа Ostrich, без неожиданных побочных эффектов.
# Принцип подстановки Барбары Лисков (Liskov Substitution Principle, LSP)


class Bird:
    pass


class FlyingBird(Bird):
    def fly(self):
        pass


class Ostrich(Bird):
    pass

# I - Не следует создавать интерфейсы, которые обязывают клиентов реализовывать методы, которые им не нужны.
# Лучше создать несколько специализированных интерфейсов.
# Если у вас есть интерфейс Worker, который имеет методы work() и eat(), и вы хотите создать класс Robot,
# то это нарушает ISP. Лучше разделить интерфейс на Workable и Eatable.
# Принцип разделения интерфейса (Interface Segregation Principle, ISP)


class Workable:
    def work(self):
        pass


class Eatable:
    def eat(self):
        pass


class Robot(Workable):
    pass


class Human(Workable, Eatable):
    pass

# D - Высокоуровневые модули не должны зависеть от низкоуровневых модулей. Оба должны зависеть от абстракций.
# Также абстракции не должны зависеть от деталей, а детали от абстракций.
# Пример: Вместо того чтобы высокоуровневый модуль напрямую зависел от низкоуровневого модуля, можно использовать
# абстракцию (интерфейс или абстрактный класс), через которую будут взаимодействовать оба модуля.
# Принцип инверсии зависимости (Dependency Inversion Principle, DIP)


class Switchable:
    def turn_on(self):
        pass

    def turn_off(self):
        pass


class LightBulb(Switchable):
    def turn_on(self):
        print("LightBulb is on")

    def turn_off(self):
        print("LightBulb is off")


class Fan(Switchable):
    def turn_on(self):
        print("Fan is on")

    def turn_off(self):
        print("Fan is off")


class ElectricPowerSwitch:
    def __init__(self, device):
        self.device = device
        self.on = False

    def press(self):
        if self.on:
            self.device.turn_off()
            self.on = False
        else:
            self.device.turn_on()
            self.on = True


# Пример использования
bulb = LightBulb()
switch = ElectricPowerSwitch(bulb)
switch.press()  # Включить лампочку
switch.press()  # Выключить лампочку

