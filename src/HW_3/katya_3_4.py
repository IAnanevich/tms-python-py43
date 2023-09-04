# Дан словарь. Добавитть каждому ключу число равное длине этого числа.

money ={'test': 'test_value',
        'europe': 'eur',
        'dollar': 'usd',
        'ruble': 'rub'}
# dick_k = list(money.keys())
# dick_v = list(money.values())
#
# n = 0
# list_new = []
# while n < len(dick_k):
#     a = f'{dick_k[n]} + {str(len(dick_k[n]))}'
#     list_new.append(a)
#     n += 1
# print(dict(zip(list_new,dick_v)))

list_new = []
for key in money.keys():
        list_new.append(f'{money[key]} {len(money)}')
print(dict(zip(list_new, list(money.values()))))
