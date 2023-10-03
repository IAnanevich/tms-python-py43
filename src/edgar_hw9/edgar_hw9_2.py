# Реализовать любой метакласс (сами придумываете что ваш метакласс будет делать)
# =============================================================================================================

class Meta(type):
    def __new__(cls, name, bases, attrs, *args, **kwargs):
        """

        :param name:
        :param attr:
        :param args:
        :param kwargs:
        """
        attrs = dict(attrs)
        attrs.update({"max_value": 25, "min_value": 0})
        return super().__new__(cls, name, bases, attrs, *args, **kwargs)

class Point(metaclass=Meta):
    def get_value(self):
        """

        :return:
        """
        return (25, 0)

pt = Point()
print(pt.get_value())
print(pt.max_value)
