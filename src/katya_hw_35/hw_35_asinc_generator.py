import asyncio


def asinc_fib(n):
    a, b = 1, 1
    for i in range(n):
        yield a
        a, b = b, a + b


async def async_main():
    async_gen_1 = asinc_fib(5)


    try:
        while True:
            value_1 = next(async_gen_1)
            print(value_1)
            await asyncio.sleep(0.5)
    except StopIteration:
        print('Генератор исчерпан')


asyncio.run(async_main())
