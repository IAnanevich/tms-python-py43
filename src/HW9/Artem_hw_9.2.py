# Реализовать любой метакласс

class MetaClass(type):
    def __new__(cls, name, base, attrs, *args, **kwargs) -> type:
        """

        :param name:
        :param base:
        :param attrs:
        :param args:
        :param kwargs:
        """
        super().__new__(cls, name, base, attrs)
        attrs.update({'l1': 12, 'l2': 14})
        return type.__new__(cls, name, base, attrs)


class Method(metaclass=MetaClass):
    def second(self):
        return f'{self.l1}'


mt = Method()
print(mt.second())
print(mt.l2)
