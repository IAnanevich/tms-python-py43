# Дан словарь:
# {'test': 'test_value', 'europe': 'eur', 'dollar': 'usd', 'ruble': 'rub'}
# Добавить каждому ключу число равное длине этого ключа
# {‘key’: ‘value’} -> {‘key3’:‘value’}).
# Чтобы получить список ключей - использовать метод .keys()

dict_before = {'test': 'test_value', 'europe': 'eur', 'dollar': 'usd', 'ruble': 'rub'}
dict_after = {f"{key}{len(key)}": value for key, value in dict_before.items()}

print(f"Before: {dict_before}")
print(f"After: {dict_after}")
