import asyncio
import time
import math


async def async_factorial(n):
    result = math.factorial(n)


async def main():
    await async_factorial(1000000)


if __name__ == '__main__':
    start_time = time.time()
    asyncio.run(main())
    end_time = time.time() - start_time

    print(f'Async factorial: {end_time:.5f} seconds')

