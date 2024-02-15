import requests
import time


def download_page(url):
    response = requests.get(url)
    # print(f"Загружена страница {url}, размер {len(response.text)}")


urls = ['http://translate.google.com' for i in range(100)]

start_time = time.time()

for url in urls:
    download_page(url)

end_time = time.time()
elapsed_time = end_time - start_time
print(f"Время выполнения без многопоточности: {elapsed_time:.3f} секунд")
