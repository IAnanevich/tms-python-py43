a = b"r\xc3\xa9sum\xc3\xa9"
print(a.decode())  # декодируем в строку байтовое значение

b = a.decode("utf-8").encode("latin1")  # преобразовываем в байтовый вид в кодировке latin1
print(b)

c = str(b, "latin1")  # декодируем в строку байтовое значение
print(c)
