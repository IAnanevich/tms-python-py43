import requests

country = input('Enter country: ')
url = f'http://universities.hipolabs.com/search?country={country}'

result = requests.get(url)
print(result.json())



