# Создать декоратор для функции, которая принимает список
# чисел.Декоратор должен производить предварительную
# проверку данных - удалять все четные элементы
# из списка.


def odd_numbers(func):
    def wrapper(list_1):
        for x in list_1:
            if x % 2:
                list_12_new.append(x)
        return list_12_new

    return wrapper


@odd_numbers
def func_int(list_x):
    return list_x


list_12 = list(range(100, 120))
list_12_new = []

print(list_12)
print(func_int(list_12))
