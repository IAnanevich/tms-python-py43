# Создать текстовый файл и записать в него 6 строк.
# Записываемые строки вводятся с клавиатуры

line_1 = str(input())
line_2 = str(input())
line_3 = str(input())
line_4 = str(input())
line_5 = str(input())
line_6 = str(input())

with open('task_string.txt', 'w') as f:
    f.write(f'{line_1} {line_2} {line_3} {line_4} {line_5} {line_6}\n')
