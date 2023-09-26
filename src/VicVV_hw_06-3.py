# При помощи функции filter() из котрежа слов отфильтровать только те, которые являются
# полиндромами (читаются одинаково в обе стороны)

words_ = ("cat", "rewire", "level", "book", "stats", "list", "АННА", "шалаш", "закаЗ")
pal_w = tuple(filter(lambda words: words == words[::-1], words_))
print("перевёртыши: ", pal_w)
