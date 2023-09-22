import prototype


def read_ip_info():
    session = prototype.Session()
    ip_info = session.query(prototype.IPInfo).all()
    session.close()
    if ip_info:
        for ip_in in ip_info:
            print(
                f'ID: {ip_in.id},'
                f'IP: {ip_in.ip},'
                f'CITY: {ip_in.city},'
                f'REGION: {ip_in.region},'
                f'COUNTRY: {ip_in.country}],'
                f'LOC: {ip_in.loc},'
                f'ORG: {ip_in.org},'
                f'POSTAL: {ip_in.postal},'
                f'TIMEZONE: {ip_in.timezone},'
                f'README: {ip_in.readme}'
            )
    else:
        print('НЕТ ДАННЫХ')