# 1. Байтовое значение: b'r\xc3\xa9sum\xc3\xa9'
# 2. Декодировать строку
# 3. Затем результат преобразовать в байтовый вид в кодировке "Latin1"
# 4. Затем результат снова декодировать в строку
# P.S. Результаты всех преобразование выводить на экран

# 1. Байтовое значение: b'r\xc3\xa9sum\xc3\xa9'
some_bytes = b"r\xc3\xa9sum\xc3\xa9"
print("\n1. Data in bytes UTF-8:", some_bytes)

# 2. Декодировать строку
some_utf8 = some_bytes.decode("utf-8")
print("\n2. String decoded:", some_utf8)

# 3. Затем результат преобразовать в байтовый вид в кодировке "Latin1"
some_bytes = some_utf8.encode("Latin1")
print("\n3. Data in bytes Latin1:", some_bytes)

# 4. Затем результат снова декодировать в строку
some_Latin1 = some_bytes.decode("Latin1")
print("\n4. String decoded:", some_Latin1)
