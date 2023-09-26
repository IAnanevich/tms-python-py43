# Декодировать

_bytes = b'r\xc3\xa9sum\xc3\xa9'
print(f'1: {_bytes}')
_str = _bytes.decode('utf-8')
print(f'2: {_str}')
_bytes = _str.encode('latin1')
print(f'3: {_bytes}')
_str = _bytes.decode('latin1')
print(f'4: {_str}')
