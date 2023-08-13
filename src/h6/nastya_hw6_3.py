"""3. При помощи функции filter() из котрежа слов отфильтровать только те,
которые являются полиндромами (которые читаются одинаково в обе стороны)."""

tup = ('tut', 'ikp', 'naan')
"""
Checking value in tuple on polyndrome
:param n: value in tuple
:return: value in tuple if value polyndrome
"""
fun = lambda n: n == n[::-1]
print(list(filter(fun, tup)))
