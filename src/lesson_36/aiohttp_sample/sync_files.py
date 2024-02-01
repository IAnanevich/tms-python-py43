import os
import requests
import time


def download(url):

    filename = os.path.basename(url)

    start_time_request = time.time()
    response = requests.get(url)
    end_time_request = time.time() - start_time_request

    print(f'Time for request in {filename}: {end_time_request:.3f} seconds')

    start_time_file = time.time()
    with open(filename, 'wb') as file:
        for chunk in response.iter_content(chunk_size=1024):
            if chunk:
                file.write(chunk)
    end_time_file = time.time() - start_time_file
    print(f'Time for writing in {filename}: {end_time_file:.3f} seconds')
    print(30*'-')


def main():
    urls = [
        'http://www.irs.gov/pub/irs-pdf/f1040.pdf',
        'http://www.irs.gov/pub/irs-pdf/f1040a.pdf',
        'http://www.irs.gov/pub/irs-pdf/f1040ez.pdf',
        'http://www.irs.gov/pub/irs-pdf/f1040es.pdf',
        'http://www.irs.gov/pub/irs-pdf/f1040sb.pdf',
    ]

    for url in urls:
        download(url)


if __name__ == '__main__':
    start_time = time.time()
    main()
    end_time = time.time() - start_time
    print(f'All time: {end_time:.3f} seconds')
