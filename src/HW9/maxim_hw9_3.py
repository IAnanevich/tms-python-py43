# Реализовать датакласс и использовать его как обьект в конструкторе для первого задания
from dataclasses import dataclass


@dataclass
class Lot:
    number_lot: int
    subject_of_purchase: str
    quantity: int | float
    value: int | float
    status: str
