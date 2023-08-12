# Дан словарь:
# {'test': 'test_value',
# 'europe': 'eur',
# 'dollar': 'usd',
# 'ruble': 'rub'}
# Добавить каждому ключу число равное длине этого ключа (пример {‘key’: ‘value’} ->
# {‘key3’:‘value’}). Чтобы получить список ключей - использовать метод .keys()

original_dictionary = {'test': 'test_value', 'europe': 'eur', 'dollar': 'usd', 'ruble': 'rub'}

updated_dict = {f"{key}{len(key)}": value for key, value in original_dictionary.items()}

print(updated_dict)
