from datetime import datetime
from models.rate import Rate
from app.bank.bank_factory import Bank
from database import session
from app.base_manager import BaseManager


class RateManager(BaseManager):
    bank_list = ["AgroPromBank", "Belarusbank"]

    def __init__(self) -> None:
        super().__init__()
        self.entity = Rate

    def update_list(self) -> None:
        # проходим по нашим банкам и ищем минимальный курс USD.
        for bank_name in self.bank_list:
            try:
                bank = Bank().get(bank_name)  # фабрика
                rate_usd = bank.get_rate()
            except Exception as e:
                print(e)
            else:
                if rate_usd > 0:
                    rate = self.get_by_bank(bank_name=bank_name)
                    if rate is None:
                        rate = self.entity(
                            code="USD",
                            bank_name=bank_name,
                            rate=rate_usd
                        )
                    else:
                        rate.rate = rate_usd
                    rate.updated_at = datetime.now()

                    self._save(rate)

    def get_by_bank(self, bank_name: str):
        return session.query(self.entity).filter_by(bank_name=bank_name).scalar()

    def remove(self, pk):
        pass
