# декодировать в строку байтовое значение b'r\xc3\xa9sum\xc3\xa9'. Затем результат преобразить в байтовый вид
# в кодировке 'Latin1' и затем результат снова декодировать в строку

line = b'r\xc3\xa9sum\xc3\xa9'

line_1 = line.decode()
print(line_1)
line_2 = line_1.encode(encoding='Latin1')
print(line_2)
line_3 = bytes.decode(line_2,'Latin1')
print(line_3)
