'''При помощи функции filter() из кортежа слов отфильтровать
только те, которые являются палиндромами(которые читаются одинаково в обе стороны).'''
words = ('эта', 'шалаш', 'программа', 'оно', 'работает', 'абоба', 'арозаупаланалапуазора')
print(tuple(filter(lambda word: word == word[::-1], words)))