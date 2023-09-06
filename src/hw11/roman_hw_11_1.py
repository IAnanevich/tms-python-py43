# Создать генератор геометрической прогрессии.
from typing import Generator


def geometric_progression(start: float, ratio: float) -> Generator[float, None, None]:
    """
    Генератор, который создает геометрическую прогрессию.

    Аргументы:
    - start (float): Начальный элемент геометрической прогрессии.
    - ratio (float): Значение, на которое умножается каждый предыдущий элемент, чтобы получить следующий.

    Возвращает:
    - Generator[float, None, None]: Генератор, возвращающий следующий элемент геометрической прогрессии.
    """
    current = start
    while True:
        yield current
        current *= ratio


gen = geometric_progression(2, 3)
for i in range(5):
    print(next(gen))
