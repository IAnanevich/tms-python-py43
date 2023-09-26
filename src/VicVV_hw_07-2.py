# Запись в файл

_str1 = input('строка 1: ')
_str2 = input('строка 2: ')
_str3 = input('строка 3: ')
_str4 = input('строка 4: ')

_file = open('example.txt', 'w')
_file.write(_str1)
_file.write('\n')
_file.write(_str2)
_file.close()

_file = open('example.txt', 'a')
_file.write('\n')
_file.write(_str3)
_file.write('\n')
_file.write(_str4)
_file.close()
