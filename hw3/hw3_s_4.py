'''Дан словарь: {'test': 'test_value', 'europe': 'eur', 'dollar': 'usd', 'ruble': 'rub'}
Добавить каждому ключу число равное длине этого ключа (пример {‘key’: ‘value’} -> {‘key3’:‘value’}).
Чтобы получить список ключей - использовать метод .keys()'''

dictionary = {'test': 'test_value', 'europe': 'eur', 'dollar': 'usd', 'ruble': 'rub'}
new_dictionary = {}
for key in dictionary.keys():
    new_key = f"{key}{len(key)}"
    new_dictionary[new_key] = dictionary[key]
print(new_dictionary)
