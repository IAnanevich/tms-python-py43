# https://pxstudio.pw/blog/15-besplatnyh-api-dlya-napisaniya-testovyh-prilozhenij
# Взять 5 любых урлов и отправить к ним запрос.
# Написать 2 программы, синхронную и асинхронную, сравнить результат выполнения по времени

import asyncio
from marina_hw36_sync import sync_get_urls  # type: ignore
from marina_hw36_async import async_get_urls  # type: ignore

list_of_urls = [
    "https://agify.io",
    "https://genderize.io",
    "https://www.ipify.org",
    "https://www.boredapi.com",
    "https://www.zippopotam.us",
]
# время работы синхронной программы
sync_time = sync_get_urls(list_of_urls)
print(f"Sync_time is: {sync_time:.2f} seconds")
# время работы асинхронной программы
async_time = asyncio.run(async_get_urls(list_of_urls))
print(f"Async_time is: {async_time:.2f} seconds")
# сравнение
faster_time = sync_time / async_time
print(f"'Sync_time' is {faster_time:.2f} times longer than 'Async_time'")
