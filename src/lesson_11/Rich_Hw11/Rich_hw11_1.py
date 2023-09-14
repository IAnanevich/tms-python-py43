# Создать генератор геометрической прогрессии

def geometric_progression(param_a, param_b, param_c):
    """
    :param param_a: one num
    :param param_b: koef progression
    :param param_c: generic element
    :return:
    """
    current = float(param_a)
    generated = 0

    while generated < int(param_b):
        yield current
        current *= float(param_c)
        generated += 1


try:
    param_a = input("Num: ")
    param_b = input("koefficent progression: ")
    param_c = input("Element: ")

    progression = geometric_progression(param_a, param_b, param_c)

    for element in progression:
        print(element)
except KeyboardInterrupt:
    print("\n End with admin")
except Exception as e:
    print(f"Error {str(e)}")
