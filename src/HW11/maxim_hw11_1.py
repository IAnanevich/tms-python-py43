# Создать генератор геометрической прогрессии

def geometric_progression(base: int) -> int:
    """ Return a geometric progression generator.

    :param base: basis of progression generator
    :return: geometric progression generator
    """
    if not isinstance(base, int):
        raise TypeError("Parameter must be integer")
    elif base == 0:
        raise ValueError("Just not zero")
    prev = base
    while True:
        yield prev
        prev *= abs(base)


if __name__ == "__main__":
    gen = geometric_progression(0)
    for _ in range(14):
        print(next(gen))
