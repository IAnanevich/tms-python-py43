import asyncio
import time
import httpx


async def send(url):
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        print(response.text)


async def main():
    urls = [
        "https://official-joke-api.appspot.com/random_joke",
        "https://catfact.ninja/fact",
        "https://www.boredapi.com/api/activity",
        "https://api.coindesk.com/v1/bpi/currentprice.json",
        "https://randomuser.me/api/"
        ]
    stime = time.time()
    tasks = [send(url) for url in urls]
    await asyncio.gather(*tasks)
    etime = time.time() - stime
    print(etime)

asyncio.run(main())
