# Сделать фунцкию деление чисел и обернутьдекоратором,
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


elem1 = float(input('Введите значение a: '))
elem2 = float(input('Введите значение b: '))

div(elem1, elem2)
