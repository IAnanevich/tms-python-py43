# Дан словарь
# Добавить каждому ключу число равное длине этого ключа (пример {‘key’: ‘value’} ->
# {‘key3’:‘value’}). Чтобы получить список ключей - использовать метод .keys()

dict_1 = {
    'test': 'test_value',
    'europe': 'eur',
    'dollar': 'usd',
    'ruble': 'rub'
    }
dict_2 = {}
list_1 = dict_1.keys()
for l_ in list_1:
    key_ = f'{l_}{len(l_)}'
    dict_2[key_] = dict_1[l_]

print(dict_1)
print(dict_2)
