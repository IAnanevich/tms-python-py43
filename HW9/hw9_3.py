# Реализовать датакласс и использовать его как обьект в конструкторе для первого задания
from dataclasses import dataclass


@dataclass
class Point2D:
    x: int = 0
    y: int = 0
