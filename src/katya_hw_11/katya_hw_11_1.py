from typing import Generator


def gen_gp(limit: int, b: float, q: float) -> Generator[float | None]:
    """

    :param limit:
    :param b:
    :param q:
    :return:
    """
    while limit >= 0:
        a = b * q
        limit -= 1
        b = a
        yield b
    if not limit:
        raise StopAsyncIteration


for i in gen_gp(limit=10, b=5, q=7):
    print(i)
