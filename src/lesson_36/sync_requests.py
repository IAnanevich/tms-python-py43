import requests
import time


def sync_task(name, url):
    print(f'Task {name} started')

    start_time = time.time()
    response = requests.get(url)
    end_time = time.time() - start_time

    print(f'Task {name} finished: {end_time:.1f}')


def sync_main():
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

    for number, url in enumerate(urls, start=1):
        sync_task(number, url)

    end_time = time.time() - start_time
    print(f'\nAll time: {end_time:.1f} seconds')


if __name__ == '__main__':
    sync_main()
    # All time: 5.5 seconds
