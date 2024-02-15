import threading
import time

import requests


def download_page(url):
    response = requests.get(url)
    # print(f"Загружена страница {url}, размер {len(response.text)}")


urls = ['http://translate.google.com' for i in range(300)]

start_time = time.time()
threads = []


for url in urls:
    thread = threading.Thread(target=download_page, args=(url, ))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

end_time = time.time()
elapsed_time = end_time - start_time
print(f"Время выполнения: {elapsed_time:.3f} секунд")
