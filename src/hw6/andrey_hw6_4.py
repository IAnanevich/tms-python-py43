#  При помощи функции filter() из котрежа слов отфильтровать только те, которые
# являются полиндромами (которые читаются одинаково в обе стороны).

print(tuple(filter(lambda x: x[::-1]==x,('1121','1221','939','0193910'))))
