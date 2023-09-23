import requests
from CreateMixin import CreateMixin
from ListMixin import ListMixin
from Homework_15.ip_models.ip_location_model import UserLocation
from sqlalchemy.orm import Session


def get_ip(session: Session) -> None:
    url_id = 'https://api.ipify.org?format=json'

    url = f'https://ipinfo.io/{url_id}/geo'
    result = requests.get(url)
    input_datar = result.json()
    new_user = CreateMixin.create(table=UserLocation, input_data=input_datar, session=session)
    session.add(new_user)
    session.commit()


def read_table(session: Session):
    result = ListMixin.list(table=UserLocation, session=session)
    for user in result:
        print(user.__dict__)
