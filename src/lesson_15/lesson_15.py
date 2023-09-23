# [user1, user2, user3] + status code
# 100-199 - информационные
# 200-299 - успешные (200 - ок, 201 - created, 204 - нет содержимого)
# 300-399 - перенаправление (301 (постоянный) и 302 (временный) - два редиректа)
# 400-499 - клиентские ошибки (
#              404 - not found, 400 - bad request, 401 - unauthorized, 403 - forbidden, 405 - method not allowed
# )
# 500-599 - серверные ошибки (500 - сервер)


# http - 80 port vs https - 443 port
# REST -
# GraphQL - query,  mutations
# gRPC -
# API - application programming interface -

import requests


key = 'cd3af24c53ee917701c4b74960e5a84d'

city = input('Enter city: ')

url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={key}'

result = requests.get(url)
print(result.json()['main'])
