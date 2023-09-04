# Реализовать любой метакласс
class RenameMethodsMeta(type):
    def __new__(cls, clsname, bases, clsdict):
        """
        :param clsname: Name of the class being created.
        :param bases: Base classes.
        :param clsdict: Dictionary of class
        """
        new_clsdict = {}
        method_count = 0

        for name, value in clsdict.items():
            if callable(value):
                method_count += 1
                new_name = f'funk_{method_count}'
                new_clsdict[new_name] = value
            else:
                new_clsdict[name] = value

        return super().__new__(cls, clsname, bases, new_clsdict)


class MyClass(metaclass=RenameMethodsMeta):
    @staticmethod
    def method_one():
        """
        print 'Method one'
        :return:
        """
        print("Method One")

    @staticmethod
    def method_two():
        """
        print Method Two
        :return:
        """
        print("Method Two")

    @staticmethod
    def not_a_method():
        """
        print Not a method
        :return:
        """
        print("Not a Method")


obj = MyClass()
obj.funk_1()
obj.funk_2()
obj.funk_3()
