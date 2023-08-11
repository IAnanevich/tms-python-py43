# При помощи функции filter() из кортежа слов отфильтровать
# только те, которые являются пfлиндронами

tuple_6_3 = ('moon', 'sagas', 'sky', 'sun', 'noon')

tuple_6_3_new = tuple(filter(lambda x: x == x[::-1], tuple_6_3))
print(tuple_6_3_new)
