# Реализовать любой метакласс (сами придумываете что ваш метакласс будет делать)

class RegistryMeta(type):
    registry = {}

    def __new__(cls, name, bases, attrs):
        new_class = super().__new__(cls, name, bases, attrs)
        cls.registry[name] = new_class
        return new_class
