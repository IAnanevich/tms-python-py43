# При помощи функции filter() из кортежа слов отфильтровать только те, которые являются полиндромами
# которые, читаются одинаково в обе стороны

words = ('nun', 'level', 'hello', 'radar', 'world')

palindromes = tuple(filter(lambda word: word == word[::-1], words))

print(palindromes)
