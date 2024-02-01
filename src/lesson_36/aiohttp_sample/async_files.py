import aiohttp
import asyncio
import os
import async_timeout
import time


async def download(session, url):

    start_time_request = time.time()

    async with async_timeout.timeout(10):
        async with session.get(url) as response:

            end_time_request = time.time() - start_time_request
            filename = os.path.basename(url)

            print(f'Time for request in {filename}: {end_time_request:.3f} seconds')

            start_time_file = time.time()

            with open(filename, 'wb') as file:
                while True:
                    chunk = await response.content.read(1024)
                    if not chunk:
                        break
                    file.write(chunk)

            end_time_file = time.time() - start_time_file
            print(f'Time for writing in {filename}: {end_time_file:.3f} seconds')

            return await response.release()


async def main(loop):
    urls = [
        'http://www.irs.gov/pub/irs-pdf/f1040.pdf',
        'http://www.irs.gov/pub/irs-pdf/f1040a.pdf',
        'http://www.irs.gov/pub/irs-pdf/f1040ez.pdf',
        'http://www.irs.gov/pub/irs-pdf/f1040es.pdf',
        'http://www.irs.gov/pub/irs-pdf/f1040sb.pdf',
    ]

    async with aiohttp.ClientSession(loop=loop, connector=aiohttp.TCPConnector(ssl=False)) as session:

        # for url in urls:
        #     await download(session=session, url=url)
        tasks = [download(session=session, url=url) for url in urls]
        await asyncio.gather(*tasks)


if __name__ == '__main__':
    start_time = time.time()

    loop = asyncio.get_event_loop()
    loop.run_until_complete(main(loop=loop))

    end_time = time.time() - start_time

    print(f'All time: {end_time:.3f} seconds')

