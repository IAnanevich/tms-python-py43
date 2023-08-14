# При помощи функции filter из кортежа слов отфильтровать полиндромы

palindrome = ('hello', 'level', 'noon', 'event')
print(tuple(filter(lambda x: x if x == x[::-1] else print(f'not palindromic: {x}'), palindrome)))
