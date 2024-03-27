import time
import requests


def sync_task(name, url):
    print(f'Task {name} started')
    start_time = time.time()

    responce = requests.get(url)

    finish_time = time.time() - start_time
    print(f'Task {name} finished: {finish_time:.5f} seconds')


def sync_prog():
    url = [
        'https://catfact.ninja/',
        'https://dog.ceo/dog-api/',
        'https://www.boredapi.com/',
        'https://official-joke-api.appspot.com/random_joke',
        'https://randomuser.me/api/',
    ]
    start_time = time.time()

    for number, url in enumerate(url, start=1):
        sync_task(number, url)

    finish_time = time.time() - start_time
    print(f'All time: {finish_time:5f} seconds')


if __name__ == '__main__':
    sync_prog()
