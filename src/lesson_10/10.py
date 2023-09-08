# a = int(input('a: '))
# b = int(input('b: '))
#
#
# print(a / b)
# try:
#     print(a / b)
# except ZeroDivisionError as error:
#     print(error)

# number = input('number: ')
#
# try:
#     number = int(number)
# except ZeroDivisionError as error:
#     print(error)
# except ValueError as error:
#     print(error)
#
# print(number)
#
# dict_ = {1: 2}
#
# print(dict_[2])


# try:
#     with open('file.txt', 'r') as file:
#         result = file.readlines()
#         if not result:
#             raise Exception('File is empty')
# except FileNotFoundError as error:
#     print(error)
# # except IOError as error:
# #     print(error)
# # except (FileNotFoundError, Exception) as error:
# #     print(error)
#
#
# print(result)


# a = int(input('a: '))
# b = int(input('b: '))
#
# try:
#     print(a / b)
# except ZeroDivisionError as error:
#     print(error)
# else:
#     print('else')  # working, when no error
# finally:
#     print('finally')  # always working


# def div(a, b):
#     try:
#         result = a / b
#     except ZeroDivisionError as error:
#         return error
#
#     result *= 2
#     return result
#
#
# print(div(10, 2))


class FileIsEmptyError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)


try:
    with open('file.txt', 'r') as file:
        result = file.readlines()
        if not result:
            raise FileIsEmptyError('File is empty')
except FileNotFoundError as error:
    print(error)
