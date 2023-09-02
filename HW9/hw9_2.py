# Реализовать любой метакласс (сами придумываете что ваш метакласс будет делать)
from hw9_3 import Point2D
from hw9_1 import (Transform2D, RigitBody)


class Validation(type):

    def __new__(cls, name, bases, dct):
        if "gravity" not in dct:
            print(f"Класс <{name}> не содержит атрибут 'gravity' !")
            dct["gravity"] = 0
        return super().__new__(cls, name, bases, dct)


class InstanceRB(RigitBody, metaclass=Validation):

    def __init__(self, coordinates: Point2D, speed: Point2D):
        super().__init__(coordinates, speed)


class InstanceTR(Transform2D, metaclass=Validation):

    def __init__(self, coordinates: Point2D, speed: Point2D):
        super().__init__(coordinates, speed)


c = Point2D(x=0, y=0)
s = Point2D(x=0, y=0)

something_1 = InstanceRB(coordinates=c, speed=s)
print(something_1)
print(something_1.gravity)

something_2 = InstanceTR(coordinates=c, speed=s)
print(something_2)
print(something_2.gravity)
