from datetime import datetime

from .api import BankApi


class AgroPromBank(BankApi):
    _api_url = "https://belapb.by/"

    # получаем курсы. возвращаем первый попавшийся USD из любого банка
    @classmethod
    def get_rate(cls) -> float:
        rates = cls.send(action="/CashExRatesDaily.php", method="get", response="xml",
                         params={'ondate': datetime.today().strftime('%m/%d/%Y')})
        # rates = cls.send(action="/CashExRatesDaily.php", method="get", response="xml",
        #                  params={'ondate': datetime.today().strftime('09/24/2023')})
        min_rate = 0
        if "Currency" in rates["DailyExRates"]:
            for i, rate in enumerate(rates["DailyExRates"]["Currency"]):
                if (rate["CharCode"] == "USD" and float(rate["RateSell"]) > 0
                        and (float(rate["RateSell"]) < min_rate or min_rate == 0)):
                    min_rate = float(rate["RateSell"])
                # TODO очень не нравится. как правильно писать, чтобы был 1 float, 1 if и без доп переменных ?
        return min_rate
