# Реализовать любой метакласс
class SimpleMetaClass(type):
    def __new__(mcs, name: str, bases, attrs) -> type:
        """

        :param name:
        :param bases:
        :param attrs:
        """
        print(f"Creating class: {name}")
        return super().__new__(mcs, name, bases, attrs)


# Применение метакласса
class MyClass(metaclass=SimpleMetaClass):
    attribute: str = "Hello"
