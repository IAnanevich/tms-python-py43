# Дан словарь:
# {'test': 'test_value',
# 'europe': 'eur',
# 'dollar': 'usd',
# 'ruble': 'rub'}
# Добавить каждому ключу число равное длине этого ключа (пример {‘key’: ‘value’} ->
# {‘key3’:‘value’}). Чтобы получить список ключей - использовать метод .keys()

original_dictionary = {'test': 'test_value', 'europe': 'eur', 'dollar': 'usd', 'ruble': 'rub'}
key_list = list(original_dictionary.keys())

for key in key_list:
    original_dictionary[key + str(len(key))] = original_dictionary.pop(key)
print(original_dictionary)