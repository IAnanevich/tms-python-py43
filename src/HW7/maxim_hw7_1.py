# Декодировать в строку байтовое значение: b'r\xc3\xa9sum\xc3\xa9'. Затем
# результат преобразовать в байтовый вид в кодировке 'Latin1' и затем результат
# снова декодировать в строку (результаты всех преобразований выводить на экран).

if __name__ == "__main__":
    byte_string = b'r\xc3\xa9sum\xc3\xa9'
    print(byte_string.decode('utf-8'),
          byte_string.decode('utf-8').encode('Latin1'),
          byte_string.decode('utf-8').encode('Latin1').decode('Latin1'),
          sep="\n")
