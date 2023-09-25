import requests
import xmltodict


class BankApi(object):
    _api_url: str
    __method = {"get", "post", "put"}

    @classmethod
    def send(cls, action: str, method: str = "get", response="json", **kwargs):
        if method not in cls.__method:
            raise "Not allow method"

        r = requests.request(method, cls._api_url + action, **kwargs)

        if response == "xml":
            return xmltodict.parse(r.content)

        return r.json()
