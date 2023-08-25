# Декодировать строку в байтовое значение b'r\xc3\xa9sum\xc3\xa9''.
# Затем результат преобразовать в байтовый вид в кодировке ‘Latin1’ и затем результат
# снова декодировать в строку, результаты всех преобразований выводить на экран.

string_code = b"r\xc3\xa9sum\xc3\xa9"  # исходная строка

print(string_code.decode("utf-8"))  # байтовое значение
print(string_code.decode("utf-8").encode("Latin1"))  # байтовое в кодировке Latin1
print(string_code.decode("utf-8").encode("Latin1").decode("Latin1"))  # строка
