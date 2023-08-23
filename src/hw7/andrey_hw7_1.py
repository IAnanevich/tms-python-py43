# Декодировать в строку байтовое значение: b'r\xc3\xa9sum\xc3\xa9'
# Затем результат преобразовать в байтовый вид в кодировке 'Latin1'
# и затем результат снова декодировать в строку (результаты всех преобразований выводить на экран).

if __name__ == "__main__":
    str_ = b'r\xc3\xa9sum\xc3\xa9'.decode()
    print(str_)
    str_ = str_.encode('Latin1')
    print(str_)
    str_ = str_.decode('Latin1')
    print(str_)
