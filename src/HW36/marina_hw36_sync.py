import requests  # type: ignore
import time


def get_url(url: str) -> None:
    """
    sends a request to url
    :param url: url for request
    :return: None
    """
    response = requests.get(url)


def sync_get_urls(list_of_urls: list[str]) -> float:
    """
    calculates sync execution time
    :param list_of_urls: list of urls for requests
    :return: time of sync receiving responses from the list of urls
    """
    start_time = time.time()
    for url in list_of_urls:
        get_url(url)
    work_time = time.time() - start_time
    return work_time
