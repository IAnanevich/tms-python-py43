""" 4. Дан словарь:
{'test': 'test_value',
'europe': 'eur',
'dollar': 'usd',
'ruble': 'rub'}
Добавить каждому ключу число равное длине этого ключа (пример {‘key’: ‘value’} ->
{‘key3’:‘value’}). Чтобы получить список ключей - использовать метод .keys()"""


d = {'test': 'test_value',
     'europe': 'eur',
     'dollar': 'usd',
     'ruble': 'rub'}
p = ['1', '2', '3', '4']
for i in zip((zip(d.keys(), p)), d.values()):
    print(i)
