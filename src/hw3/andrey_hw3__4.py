'''
Дан словарь:
{'test': 'test_value',
 'europe': 'eur',
 'dollar': 'usd',
 'ruble': 'rub'}
Добавить каждому ключу число равное длине этого ключа
(пример
{‘key’: ‘value’} ->
{‘key3’:‘value’}).
Чтобы получить список ключей - использовать метод.keys()
'''

dict_ = {'test': 'test_value',
         'europe': 'eur',
         'dollar': 'usd',
         'ruble': 'rub'}

print({i + str(len(i)): dict_[i] for i in dict_.keys()})
