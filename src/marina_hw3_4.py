# Дан словарь:
# {'test': 'test_value',
# 'europe': 'eur',
# 'dollar': 'usd',
# 'ruble': 'rub'}
# Добавить каждому ключу число равное длине этого ключа (пример {‘key’: ‘value’} ->
# {‘key3’:‘value’}). Чтобы получить список ключей - использовать метод .keys()

dict_currency = {'test': 'test_value', 'europe': 'eur', 'dollar': 'usd', 'ruble': 'rub'}

for key_c in tuple(dict_currency.keys()):
    dict_currency[key_c + str(len(key_c))] = dict_currency[key_c]  # TODO убрать конкатенацию
    del dict_currency[key_c]

print(dict_currency)
