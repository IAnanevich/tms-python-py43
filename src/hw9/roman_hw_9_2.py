# Реализовать любой метакласс
class SimpleMetaClass(type):
    def __new__(cls, name, bases, attrs):
        """

        :param name:
        :param bases:
        :param attrs:
        """
        print(f"Creating class: {name}")
        return super().__new__(cls, name, bases, attrs)


# Применение метакласса
class MyClass(metaclass=SimpleMetaClass):
    attribute = "Hello"
