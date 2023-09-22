import requests
from requests import Session
import prototype


def create_ip_info():
    response = requests.get("https://ipinfo.io/161.185.160.93/geo")
    if response.status_code == 200:
        ip_data = response.json()
        session = Session()
        for _ in ip_data:
            ip_info = prototype.IPInfo(
                ip=ip_data['ip'],
                city=ip_data['city'],
                region=ip_data['region'],
                country=ip_data['country'],
                loc=ip_data['loc'],
                org=ip_data['org'],
                postal=ip_data['postal'],
                timezone=ip_data['timezone'],
                readme=ip_data['readme']
            )
            session.add(ip_info)
        session.commit()
        session.close()
        print('УСПЕШНО')
    else:
        print('ПРОБЛЕМЫ С API')