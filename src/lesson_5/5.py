from typing import Union, Optional

# def main():
#     return 1
#
#
# def add(a, b):
#     return a + b
#
#
# def increase(a, b):
#     return a - b
#
#
# print(main())
# print(add(1, 2))
# print(add(a=1, b=2))
# print(increase(b=1, a=2))


# def format_str(string, char='.'):  # hello -> hello!
#     return f'{string}{char}'


# print(format_str(string='hello', char='!'))
# print(format_str(string='hello'))


# *args, **kwargs
# def main(age, name, *args):
#     print(args[0])
#     print(type(args))
#
#
# main(1, 2, 3, 4, 5, 6)


# def main(info, *args, **kwargs):
#     print(f'info = {info}')
#     print(f'args = {args}')
#     print(f'kwargs = {kwargs}')
#
#
# main('It', 2, 3, 4, age=10, name='Ivan', city='Minsk')


# def my_func(**kwargs):
#     keys, values = [], []
#     for key, value in kwargs.items():
#         print(key, value)
#         keys.append(key)
#         values.append(value)
#     return keys, values
#
#
# keys, values = my_func(a=5, b=3)
# print(keys, values)


# def add(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
#     return a + b


# def add(a: int | float, b: int | float = 1) -> int | float:
#     return a + b
#
#
# def main(list_of_students: list[str | int]) -> list[str]:
#     return list_of_students
#
#
# def main_2(
#     a: int | None  # Optional[int]
# ):
#     return a
#
#
# print(add('a', 'b'))


# def main(
#     a: int | float,
#     b: int | float,
#     c: int | float,
#     d: int | float,
#     e: int | float,
#     f: int | float,
#     g: int | float,
#     h: int | float
# ) -> int | float:
#     return a


# def main():
#     pass
#
#
# for i in range(10):
#     pass
#
#
# if 5 > 2:
#     pass
# else:
#     pass


# def main(a, b):
#     print(x)
#     # x += 1
#     y = 10
#     # print(x)
#
#
# x = 4
# main(1, 2)
# print(y)


# def main_2(x):
#     # print(x)
#     global x
#     x = 20
#
#
# main_2(x)
# print(x)


# x = "awesome"
#
#
# def myfunc(y):
#     global x
#     print(y)
#     x = "fantastic"
#
#
# myfunc(x)
#
# print("Python is " + x)


# def main():
#     global x
#     x = 10
#     print(x)
#
#     def main2():
#         global x
#         x += 1
#         print(x)
#
#     main2()
#
# main()

# a = [i * 2 for i in range(1, 5) if not i % 2]

# a = [i if i > 4 else 'less than 4' for i in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]]

# info = {'name': 'ivan', 'age': 23}
#
# a = {f'{key}{len(key)}': value for key, value in info.items()}

# a = []
# for i in range(1, 5):
#     if not i % 2:
#         a.append(i * 2)
# print(a)
