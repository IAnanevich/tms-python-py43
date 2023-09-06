def gen_gp(limit: int, b: int, q: int):
    while limit >= 0:
        a = b * q
        limit -= 1
        b = a
        yield b
    if not limit:
        raise StopAsyncIteration


gt = gen_gp(limit=10, b=5, q=7)
for i in gt:
    print(i)
