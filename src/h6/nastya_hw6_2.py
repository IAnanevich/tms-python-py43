""" 2. Дан список чисел. Вернуть список, где при помощи функции тар()
каждое число переведено в строку. В качестве функции в mар использовать lambda."""

list_ = [1, 2, 3, 4, 1]
"""
Makes each value in the list str
:param n: value in the list
:return: value in type str
"""
fun = lambda n: str(n)
print(list(map(fun, list_)))
