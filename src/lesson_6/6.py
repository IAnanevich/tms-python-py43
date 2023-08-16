# from functools import reduce
# from typing import Callable
from functools import wraps


# def add(a: int, b: int) -> int:
#     """
#     Adding first number to second
#     :param a: first number
#     :param b: second number
#     :return: summa of 2 numbers
#     """
#     return a + b
#
#
# print(add.__name__)

# number = lambda x, y: x * y  # variable = lambda arg1, arg2, ... : expression
# print(number(10, 20))
#
#
# def number_func(x, y):
#     return x * y
#
#
# tables = [lambda x=x: x * 10 for x in range(1, 5)]
# for table in tables:
#     print(table())
#
#
# max_number = lambda a, b: a if a > b else b
# print(max_number(10, 2))


# def square(elem):
#     return elem ** 2


# numbers = [1, 2, 3, 4, 5]
# new_numbers = list(map(lambda i: i ** 2 + 10, numbers))
#
# print(new_numbers)

# new_numbers = []
# for i in numbers:
#     new_numbers.append(square(i))
#
# print(new_numbers)


# def map(func, iterable):
#     result = []
#     for item in iterable:
#         result.append(func(item))
#     return result


# def greater(num):
#     return num > 6


# numbers = [2, 3, 7, 9, 10, 1, -5]
# result = []
# for i in numbers:
#     if greater(i):
#         result.append(i)
#
# print(result)

# result = list(filter(lambda x: x > 6, numbers))
# print(result)

# def filter(func, iterable):
#     result = []
#     for item in iterable:
#         if func(item):
#             result.append(item)
#     return result


# def mult(res, elem):
#     return res * elem
#
#
# numbers = [2, 3, 7, 9, 10, 1, -5]
# result = 1
# for i in numbers:
#     result = mult(result, i)
#
# print(result)


# def reduce(func, iterable, initial):
#     result = initial
#     for item in iterable:
#         result = func(result, item)
#     return result

# initial = -1
# result = reduce(lambda x, initial: x * initial, numbers, initial)
# print(result)


# def main(func: Callable):
#     # if not isinstance(func, Callable):
#     #     return None
#     try:
#         a = func(1, 2)
#     except TypeError as e:
#         return e
#
#     return a
#
#
# print(main(1))


# def main(a):
#     return a


# print(max([1, 2, 3, 4, 5]))
# print(min([2, 2, 2], key=main))

# sample_dict = {1: 20, 3: 4, -5: 6, -7: 8}
# key_two = min(sample_dict, key=lambda k: sample_dict[k])
# print("The key with the smallest value in sample_dict:", key_two)


# def mult(num_1):
#     var = 10
#     list_ = [1, 2, 3]
#
#     def inner(num_2):
#         nonlocal var
#         list_.append(4)
#         print(list_)
#         var += 1
#         print(var)
#         return num_1 * num_2
#
#     def inner_2(num_2):
#         nonlocal var
#         list_.append(4)
#         print(list_)
#         var += 1
#         print(var)
#         return num_1 + num_2
#
#     a = inner(10)
#     b = inner_2(10)
#
#     return inner, inner_2, var
#

# inner, inner_2, var = mult(5)
#
# print(inner_2(10))
# print(var)

# print(result.__closure__[0].cell_contents)


# def decorator(func):
#     @wraps(func)
#     def inner(*args, **kwargs):
#         print(1)
#         func()
#         print(2)
#         # func()
#         return
#
#     return inner


# @decorator
# def say():
#     print('Hello world')


# # say()
# result = decorator(say)
# result()
# say()
# print(say.__name__)


# def decorator(func):
#     @wraps(func)
#     def wrapper(*args, **kwargs):
#         return func(*args, **kwargs)
#     return wrapper
#
#
# @decorator
# def string_upper(string):
#     return string.upper()
#
#
# print(string_upper('hello'))
# print(f'{string_upper.__name__}')

# def html(tag_start: str, tag_end):
#
#     def decorator(func):
#
#         @wraps(func)
#         def inner(*args, **kwargs):
#             print(f'{tag_start}', end='')
#             func(*args, **kwargs)
#             print(f'{tag_end}')
#         return inner
#
#     return decorator
#
#
# @html(tag_start='<h1>', tag_end='</h1>')
# def say(name):
#     print(f'Hello {name}', end='')


# @html(tag='h2')
# def text(age):
#     print(f'My age: {age}', end='')
#
#
# @html(tag='href')
# def link(url):
#     print(f'URL is: {url}', end='')
#

# say('Petya')
# text(10)
# link('https://www.youtube.com/')

# <h1> say() </h1>
# <h2> text() </h2>


def stars(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("*" * 30)
        return func(*args, **kwargs)

    return wrapper


def lines(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("-" * 30)
        return func(*args, **kwargs)

    return wrapper


def equals(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("=" * 30)
        return func(*args, **kwargs)

    return wrapper


@stars
@lines
@equals
def main(a, b):
    return a + b


print(main(4, 5))
