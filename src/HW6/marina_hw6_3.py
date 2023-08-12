# При помощи функции filter() из кортежа слов отфильтровать только те, которые являются палиндромами.

words_tuple = ('казак', 'hell', 'цирк', 'замок', 'mom')

print(tuple(filter(lambda word: word == word[::-1], words_tuple)))
