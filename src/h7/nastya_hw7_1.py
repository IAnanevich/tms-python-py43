"""1. Декодировать в строку байтовое значение: b'r\xc3\xa9sum\xc3\xa9'.
Затем результат преобразовать в байтовый вид в кодировке 'Latin1' и
затем результат снова декодировать в строку (результаты всех преобразований выводить на экран)."""

print(b'r\xc3\xa9sum\xc3\xa9'.decode())
print(b'r\xc3\xa9sum\xc3\xa9'.decode().encode('Latin1'))
print(b'r\xc3\xa9sum\xc3\xa9'.decode().encode('Latin1').decode('utf-16'))
