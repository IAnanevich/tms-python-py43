# При помощи функции filter() из кортежа слов отфильтровать только те, которые
# являются палиндромами (которые читаются одинаково в обе стороны).

if __name__ == "__main__":
    print(list(filter(lambda x: x == ''.join(reversed(x)) if x.isalpha() and len(x) > 2 else '',
                      ("odd", "dodo", "level", "a", "", "tenet"))))
