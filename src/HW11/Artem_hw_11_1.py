from typing import Generator, Any


def progression(first: int, q: int) -> Generator[int, Any, None]:
    """

    :param first: the first element of the progression
    :param q: the denominator of the progression
    :return: geometric progression
    """
    while True:
        cur = first * q
        first = cur
        yield cur


a = progression(1, 2)
for _ in range(5):
    print(next(a))
