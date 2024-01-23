import asyncio

# event loop, coroutine, futures


async def print_numbers_1():
    for i in range(1, 101):
        print(i)
        await asyncio.sleep(0.3)


async def print_numbers_2():
    for i in range(101, 201):
        print(i)
        await asyncio.sleep(0.3)


async def main():
    task1 = asyncio.create_task(print_numbers_1())
    task2 = asyncio.create_task(print_numbers_2())

    await asyncio.gather(task1, task2)


asyncio.run(main())
