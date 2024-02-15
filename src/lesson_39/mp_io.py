import requests
import multiprocessing
import time


def download_page(url):
    response = requests.get(url)
    # print(f"Загружена страница {url}, размер {len(response.text)}")


if __name__ == '__main__':

    urls = ['http://translate.google.com' for i in range(300)]

    start_time = time.time()
    processes = []

    for url in urls:
        process = multiprocessing.Process(target=download_page, args=(url, ))
        processes.append(process)
        process.start()

    for process in processes:
        process.join()

    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Время выполнения: {elapsed_time:.3f} секунд")
