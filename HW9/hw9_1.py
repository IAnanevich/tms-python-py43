from math import sqrt
from hw9_3 import Point2D


# Реализовать любой класс на свой выбор.
# Несколько методов (один обязательно статикметод, один классметод, один обычный, один метод протектед)
class Transform2D:

    # В нем сделать конструктор
    def __init__(self, coordinates: Point2D, speed: Point2D):
        self.point_x = coordinates.x
        self.point_y = coordinates.y
        self.speed_x = speed.x
        self.speed_y = speed.y

    def is_moving(self) -> bool:
        """
        Возвращает статус - находится ли объект в движении
        :return: True - если движется, False - неподвижен
        """
        if self.speed_x == 0 and self.speed_y == 0:
            return False
        return True

    @staticmethod
    def who_is() -> None:
        """
        No comments
        :return: Ничего
        """
        print("I'am Grooot!")

    def add_force(self, force: Point2D, time_in_seconds: float) -> None:
        """
        Прикладывает силу к объекту по осям, на протяжении указаного времени
        :param force: вектор силы
        :param time_in_seconds: время воздействия
        :return: Ничего
        """
        self.speed_x += time_in_seconds * force.x
        self.speed_y += time_in_seconds * force.y

    def _teleport(self, coordinates: Point2D) -> None:
        """
        Мгновенная телепортация в точку
        :return: Ничего
        """
        self.point_x = coordinates.x
        self.point_y = coordinates.y

    def __gt__(self, other) -> float:
        """
        Сравнение скоростей
        :param other: как обычно
        :return: скорость объекта по вектору
        """
        return sqrt(self.speed_x ** 2 + self.speed_y ** 2) > other


print("\n TRANSFORM")
new_body = Transform2D(coordinates=Point2D(x=0, y=0), speed=Point2D(x=0, y=0))
print("moving: ", new_body.is_moving())

add_force = Point2D(x=10, y=20)
new_body.add_force(force=add_force, time_in_seconds=1.25)
print("moving: ", new_body.is_moving())
print("is speed greater then 1? = ", new_body > 1)


# Сделать два класса дочерних.
# В этих классах переопределить все методы и конструктор,
# которые можете (один метод должен быть переопределен ТОЛЬКО ОДИН раз в любом классе ребенке)
# Сделать проверку, что все работает (создать обьекты от классов)
class VerticalLift(Transform2D):

    # В нем сделать конструктор
    def __init__(self, coordinates: Point2D, speed: Point2D):
        super().__init__(coordinates, speed)
        self.speed_x = 0

    def add_force(self, force: Point2D, time_in_seconds: float) -> None:
        """
        Прикладывает силу к объекту по осям, на протяжении указаного времени
        :param force: вектор силы, но только для оси Y
        :param time_in_seconds: время воздействия
        :return: Ничего
        """
        self.speed_y += time_in_seconds * force.y


class RigitBody(Transform2D,):

    # В нем сделать конструктор
    def __init__(self, coordinates: Point2D, speed: Point2D):
        super().__init__(coordinates, speed)
        self.gravity = 9.6

    def add_force(self, force: Point2D, time_in_seconds: float) -> None:
        """
        Прикладывает силу к объекту по осям, на протяжении указаного времени, с учетом гравитации
        :param force: вектор силы
        :param time_in_seconds: время воздействия
        :return: Ничего
        """
        self.speed_x += time_in_seconds * force.x
        self.speed_y += time_in_seconds * (force.y - self.gravity)


# Lift
print("\n LIFT")
lift = VerticalLift(coordinates=Point2D(x=1, y=0), speed=Point2D(x=1, y=1))
print("moving: ", lift.is_moving())
add_down_force = Point2D(x=10, y=-1)
lift.add_force(force=add_down_force, time_in_seconds=1)
print("moving: ", lift.is_moving())
print("is speed greater then 1? = ", lift > 1)

# Fly
print("\n FLY")
fly = RigitBody(coordinates=Point2D(x=5, y=5), speed=Point2D(x=0, y=10))
print("moving: ", fly.is_moving())
add_force = Point2D(x=10, y=9)
fly.add_force(force=add_force, time_in_seconds=1)
print("moving: ", fly.is_moving())
print("is speed greater then 1? = ", fly > 1)
