"""
из pdf текст копируется криво. но суть ясна думаю
1. : Декодировать  в с файломтроку байтовое з example.txtначение b'r\xc3\xa9sum\xc3\xa9' r')Затем
рез example.txtуль тат преобраз example.txtовать  в байтовый вид в кодировке ‘Latin1’ и затем результат Latin('example.txt','r') ’ и затем результат  и з example.txtатем рез example.txtуль тат 1
с файломнова декодировать  в с файломтроку рез example.txtуль таты вс файломех преобразований выводить на экран). преобраз example.txtований выводить  на экран ( ).
"""

str_1 = b"r\xc3\xa9sum\xc3\xa9".decode()
print(str_1)
str_2 = str_1.encode("Latin1")
print(str_2)
str_1 = str_2.decode("Latin1")
print(str_1)
