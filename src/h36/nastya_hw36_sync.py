import time
import requests


def send(url):
    response = requests.get(url)
    print(response.text)


def main():
    urls = [
        "https://official-joke-api.appspot.com/random_joke",
        "https://catfact.ninja/fact",
        "https://www.boredapi.com/api/activity",
        "https://api.coindesk.com/v1/bpi/currentprice.json",
        "https://randomuser.me/api/"
        ]
    stime = time.time()
    for url in urls:
        send(url)
    etime = time.time() - stime
    print(etime)


main()
