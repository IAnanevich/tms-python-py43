import time
import httpx
import asyncio


async def async_task(name, url):
    print(f'task {name} started')
    start_time = time.time()

    async with httpx.AsyncClient() as client:
        responce = await client.get(url)

    finish_time = time.time() - start_time
    print(f'Task {name} finished: {finish_time:.5f} seconds')


async def sync_prog():
    urls = [
        'https://catfact.ninja/',
        'https://dog.ceo/dog-api/',
        'https://www.boredapi.com/',
        'https://official-joke-api.appspot.com/random_joke',
        'https://randomuser.me/api/',
    ]
    start_time = time.time()

    tasks = [async_task(number, url) for number, url in enumerate(urls, start=1)]
    await asyncio.gather(*tasks)

    finish_time = time.time() - start_time
    print(f'All time: {finish_time:5f} seconds')


if __name__ == '__main__':
    asyncio.run(sync_prog())
