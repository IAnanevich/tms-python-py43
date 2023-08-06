# Дан словарь:
# {'test': 'test_value', 'europe': 'eur',
# 'dollar': 'usd', 'ruble': 'rub'}
# Добавить каждому ключу число длине этого ключа
# (пример{'key':'value'} - > {'key3':'value'}).
# Чтобы получить списко ключей - использовать метод .keys().

my_dict = {'test': 'test_value', 'europe': 'eur', 'dollar': 'usd', 'ruble': 'rub'}
print({i + str(len(i)): my_dict[i] for i in my_dict.keys()})
