# class User:
#
#     def __init__(self, name: str, age: int) -> None:
#         self.name = name
#         self.age = age
#
#     @property
#     def get_name(self):
#         return self.name
#
#     def info(self):
#         return f'I am {self.get_name()}'
        # return f'I am {self.name}'
    #
    # @staticmethod
    # def hello():
    #     print(User(name='Petr', age=10).info())
        # return 'Hello world'
    #
    # @classmethod
    # def some_method(cls):
    #     print(cls.mro())
    #
    # @classmethod
    # def get_cls(cls):
    #     print(cls)
    #
    # def get_self(self):
    #     print(self)
#
#
# User(name='Petr', age=10).hello()
# user = User(name='Petr', age=10)
# user.some_method()
# user.get_cls()
# user.get_self()

# print(user.get_name)


# class Coordinate:
#
#     def __init__(self, x, y, z):
#         self.x = x
#         self.y = y
#         self.z = z


# @dataclass(order=True)  # __init__, __repr__, __eq__
# class Coordinate:
#     x: float
#     y: float
#     z: float = 10
#
#     @property
#     def get_x(self):
#         return self.x
#
#
# point_1 = Coordinate(1, 2)
# print(point_1)
# point.z = 20
# print(point)
# print(point.get_x)
# point_2 = Coordinate(100, 100)
# print(point_1 < point_2)  # (1, 2, 10) < (100, 100, 10)
# print(asdict(point_1))
# print(astuple(point_2))


# @dataclass(slots=True)
# class Person:
    # __slots__ = ('name', 'age')
    # name: str
    # age: int
    # is_admin: bool = False


# @dataclass(slots=True)
# class Employee(Person):
    # __slots__ = super().__slots__ + ('salary', )
    # salary: int


# employee_1 = Employee(name='Petr', age=25, salary=1000)
# print(employee_1)
# print(employee_1.__slots__)


# def create_class():
#     class Foo(object):
#         pass
#     return Foo
#
#
# foo = create_class()
# print(foo())


# print(type(1))
# print(type('1'))


# def get_name(self):
#     return self.name
#
#
# my_class = type('MyClass', (), {'name': 'Petr', 'get_name': get_name})  # name, bases (родительские классы), attrs (аттрибуты класса)
# print(my_class().name)
# print(my_class().get_name())


# class Foo(metaclass=something, kwarg1=value1, ...):


# class MyMetaClass(type):
#     pass
#
#
# class Foo(metaclass=MyMetaClass):
#     pass


# class UpperAttrMetaclass(type):
#     def __new__(
#         cls,
#         future_class_name,
#         future_class_parents,
#         future_class_attr
#     ):
#
#         uppercase_attr = {}
#         for name, val in future_class_attr.items():
#             if not name.startswith('__'):
#                 uppercase_attr[name.upper()] = val
#             else:
#                 uppercase_attr[name] = val
#
#         # повторно используем метод type.__new__,
#         # это базовое ООП, в нем нет ничего волшебного
#         return type.__new__(
#             cls,
#             future_class_name,
#             future_class_parents,
#             uppercase_attr
#         )
#
#
# class Foo(metaclass=UpperAttrMetaclass):
#     bar = 'bip'
#
#
# f = Foo()
# print(hasattr(Foo, 'bar'))
# print(hasattr(Foo, 'BAR'))
# print(f.BAR)


class TypeCheckMeta(type):
    def __new__(cls, name, bases, attrs):
        # Проходимся по всем атрибутам класса
        for attr_name, attr_value in attrs.items():
            # Проверяем, является ли атрибут функцией
            if callable(attr_value):
                # Заменяем оригинальный метод на обертку с проверкой типов
                attrs[attr_name] = cls.wrap_method(attr_value)

        return super().__new__(cls, name, bases, attrs)

    @staticmethod
    def wrap_method(method):
        def wrapper(*args, **kwargs):
            # Получаем аннотации аргументов метода
            annotations = method.__annotations__

            # Проверяем типы аргументов
            for arg_name, arg_type in annotations.items():
                if arg_name in kwargs:
                    if not isinstance(kwargs[arg_name], arg_type):
                        raise TypeError(f"Argument '{arg_name}' must be of type {arg_type.__name__}")
                elif arg_name in args:
                    arg_index = args.index(arg_name)
                    if not isinstance(args[arg_index], arg_type):
                        raise TypeError(f"Argument '{arg_name}' must be of type {arg_type.__name__}")

            return method(*args, **kwargs)

        return wrapper
