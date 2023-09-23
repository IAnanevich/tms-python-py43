import requests
import sys
sys.path.append('../')
from mixins.create_mixin import CreateMixin
from mixins.read_mixin import ReadMixin
from models.currencies_rates_model import Rates
from sqlalchemy.orm import Session
from datetime import datetime


class RatesManager(CreateMixin, ReadMixin):

    @classmethod
    def add_rates(cls, session: Session, currency: str = "840"):
        url = f"https://api.nbrb.by/exrates/rates/{currency}?parammode=1"
        result = requests.get(url)
        input_data = result.json()
        input_data["Date"] = datetime.strptime(input_data["Date"], '%Y-%m-%dT%H:%M:%S')
        cls.create(table=Rates, input_data=input_data, session=session)

    @classmethod
    def draw_rates(cls, session: Session):
        result = cls.read(table=Rates, session=session)
        print("="*25)
        for i in result:
            print(i.Cur_Name, i.Cur_Abbreviation, i.Cur_Scale, i.Cur_OfficialRate)
        print("=" * 25)
