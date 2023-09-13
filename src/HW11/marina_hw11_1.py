# Создать генератор геометрической прогрессии.
from typing_extensions import Generator


def geometry_progression(
    base: float | int, ratio: float | int, n: int
) -> Generator[float | int, None, None]:
    """
    generator of numbers of geometry progression
    :return: generator
    """
    for _ in range(n):
        yield base
        base **= ratio


for i, numb in enumerate(geometry_progression(base=2, ratio=0.5, n=5), 1):
    print(f"{i} term of a geometric progression is: {numb}")
