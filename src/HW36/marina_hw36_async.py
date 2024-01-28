import asyncio
import time
import httpx


async def async_get_url(url: str) -> None:
    """
    sends an async request to url
    :param url: url for request
    :return: None
    """
    async with httpx.AsyncClient() as client:
        response = await client.get(url)


async def async_get_urls(list_of_urls: list[str]) -> float:
    """
    calculates async execution time
    :param list_of_urls: list of urls for requests
    :return: time of async receiving responses from the list of urls
    """
    start_time = time.time()
    tasks = [async_get_url(url) for url in list_of_urls]
    await asyncio.gather(*tasks)
    work_time = time.time() - start_time
    return work_time
