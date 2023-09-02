# При помощи функции filter() из кортежа слов отфильтровать только те,
# которые являются полиндромами которые, читаются одинаково в обе стороны

some_words = ("12321", "100500", "9998", "oddo", "nope")

filtred_words = tuple(filter(lambda s: s == s[::-1], some_words))

print(filtred_words)
