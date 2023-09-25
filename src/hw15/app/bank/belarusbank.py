from .api import BankApi


class Belarusbank(BankApi):
    _api_url = "https://belarusbank.by/api"

    # получаем курсы. возвращаем первый попавшийся USD
    @classmethod
    def get_rate(cls) -> float:
        rates = cls.send(action="/kursExchange", method="get", params={'city': 'Брест'})
        min_rate = 0
        if rates:
            for i, rate in enumerate(rates):
                if (float(rate["USD_out"]) > 0 and
                        (float(rate["USD_out"]) < min_rate or min_rate == 0)):
                    min_rate = float(rate["USD_out"])
                # TODO очень не нравится. как правильно писать, чтобы был 1 float, 1 if и без доп переменных ?

        return min_rate
