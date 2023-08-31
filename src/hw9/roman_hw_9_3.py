# Реализовать датакласс и использовать его как обьект в конструкторе для первого задания
from dataclasses import dataclass


@dataclass
class DataObject:
    attribute1: str
    attribute2: int
    attribute3: list


class MyClass:
    def __init__(self, data: DataObject):
        """

        :param data:
        """
        self.data = data


data_obj = DataObject("Hello", 42, [1, 2, 3])
my_object = MyClass(data_obj)

print(my_object.data.attribute1)  # Output: Hello
print(my_object.data.attribute2)  # Output: 42
print(my_object.data.attribute3)  # Output: [1, 2, 3]
