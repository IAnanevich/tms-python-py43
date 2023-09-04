# Реализовать любой метакласс (сами придумываете что ваш метакласс будет делать)


class Meta(type):
    def __new__(cls, name, base, attrs, *args, **kwargs):
        """

        :param name:
        :param base:
        :param attrs:
        :param args:
        :param kwargs:
        """
        attrs.update({"max_value": 100, "min_value": 0})
        return super().__new__(cls, name, base, attrs, *args, **kwargs)


class Point(metaclass=Meta):
    def get_value(self):
        """

        :return:
        """
        return (300, 0)


pt = Point()
print(pt.get_value())
print(pt.max_value)
