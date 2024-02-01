import asyncio
import aiohttp
import time


async def task(name, queue):

    print(f'Task {name} started')
    results = {}

    while not queue.empty():
        url = await queue.get()
        start_time = time.time()

        async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(ssl=False)) as session:

            async with session.get(url) as response:
                result_text = await response.text()

        end_time = time.time() - start_time
        print(f'Task {name} finished: {end_time:.5f} seconds')
        results[url] = result_text[:20]

    return results


async def main():

    work_queue = asyncio.Queue()

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

    for url in urls:
        await work_queue.put(url)

    start_time = time.time()

    results = await asyncio.gather(
        asyncio.create_task(task('1', work_queue)),
        asyncio.create_task(task('2', work_queue)),
        asyncio.create_task(task('3', work_queue)),
        asyncio.create_task(task('4', work_queue)),
        asyncio.create_task(task('5', work_queue)),
        # asyncio.create_task(task('6', work_queue)),
        # asyncio.create_task(task('7', work_queue)),
        # asyncio.create_task(task('8', work_queue)),
        # asyncio.create_task(task('9', work_queue)),
        # asyncio.create_task(task('10', work_queue)),
    )

    end_time = time.time() - start_time

    print(f'\nAll finished: {end_time:.1f} seconds')
    return results


if __name__ == '__main__':
    print(asyncio.run(main()))
