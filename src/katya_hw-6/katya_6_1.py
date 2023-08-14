# Сделать фунцкию деление чисел и обернуть декоратором,
# который проверял бы деление на ноль, и отказывал в
# работе пользователю


def div_0(func):
    def wrapper(elem1, elem2):
        if elem2 == 0:
            print('Делить на ноль нельзя')
        else:
            print(func(elem1, elem2))
    return wrapper


@div_0
def div(elem1: float, elem2: float) -> float:
    """
    Calculating the dividing
    :param elem1: first number
    :param elem2: second number
    :return: the dividing the first number by the second numbers
    """
    return elem1 / elem2


while True:
    elem1 = input('Введите значение a: ')
    elem2 = input('Введите значение b: ')

    if elem1.isdigit() and elem2.isdigit():
        div(float(elem1), float(elem2))
        break
    else:
        print('Введите числовое значение')
