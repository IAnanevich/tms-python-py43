# Декодировать в строку байтовое значение: b'r\xc3\xa9sum\xc3\xa9'.
# Затем результат преобразовать в байтовый вид в кодировке "Latin1" и затем результат снова декодировать в строку.
# (результаты всех преобразование выводить на экран).
# =================================================================================================================

original_bytes = b'r\xc3\xa9sum\xc3\xa9'

# Conversion to byte form in "Latin1" encoding

latin1_bytes = original_bytes.decode("utf-8").encode("latin1")
print("Latin1 bytes: ", latin1_bytes)

# Decoding to string from byte view in "Latin1" encoding

decoded_string = latin1_bytes.decode("latin1")
print("Decoded string: ", decoded_string)
