import asyncio
import time
import httpx


async def async_task(name, url):
    print(f'Task {name} started')

    start_time = time.time()

    async with httpx.AsyncClient() as client:
        response = await client.get(url)

    end_time = time.time() - start_time
    print(f'Task {name} finished: {end_time:.5f} seconds')


async def async_main():

    urls = [
        'http://apple.com',
        'http://google.com',
        'http://yahoo.com',
        'http://facebook.com',
        'http://linkedin.com',
        'http://youtube.com',
        'http://microsoft.com',
        'http://translate.google.com',
        'http://github.com',
        'http://gitlab.com',
    ]

    start_time = time.time()

    tasks = [async_task(number, url) for number, url in enumerate(urls, start=1)]
    await asyncio.gather(*tasks)

    end_time = time.time() - start_time
    print(f'\nAll time: {end_time:.1f} seconds')


if __name__ == '__main__':
    asyncio.run(async_main())
