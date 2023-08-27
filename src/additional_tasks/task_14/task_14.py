# В конец существующего текстового файла записать три новые строки текста.
#Записываемые строки вводятся с клавиатуры.

line_1 = str(input())
line_2 = str(input())
line_3 = str(input())

with open('task_string.txt', 'a') as f:
    f.write(f'{line_1} {line_2} {line_3}\n')
