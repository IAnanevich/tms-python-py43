'''Декодировать в строку байтовое значение: b'r\xc3\xa9sum\xc3\xa9'.
Затем результат преобразовать в байтовый вид в кодировке Latin1 и затем
результат снова декодировать в строку результаты всех преобразований выводить на экран.'''
byte_value = b'r\xc3\xa9sum\xc3\xa9'.decode('utf-8')
print(f'Декодированная строка: {byte_value}')
latin_one = byte_value.encode('latin1')
print(f'Байтовый вид в кодировке Latin1: {latin_one}')
final_str = latin_one.decode('latin1')
print(f'Конечная декодированная строка: {final_str}')
