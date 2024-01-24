import asyncio
from time import sleep


def async_generator_1():
    for i in range(5):
        sleep(3)
        yield i


def async_generator_2():
    for i in range(10, 15):
        sleep(3)
        yield i


async def async_main():
    async_gen_1 = async_generator_1()
    async_gen_2 = async_generator_2()

    try:
        while True:
            value_1 = next(async_gen_1)
            print(value_1)
            value_2 = next(async_gen_2)
            print(value_2)
    except StopIteration:
        pass


asyncio.run(async_main())
