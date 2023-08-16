# Ввести с клавиатуры 4 строки и сохранить их в 4 разные переменные.
# Создать файл и записать в него первые 2 строки и закрыть файл.
# Затем открыть файл на редактирование и дозаписать оставшиеся 2 строки.
# В итоговом файле должны быть 4 строки, каждая из которых должна начинаться с новой строки.

lines = []
for i in range(4):
    line = input(f"Enter line {i + 1}: ")
    lines.append(line)

# Writing the first 2 lines to a file
with open('output.txt', 'w') as file:
    for line in lines[:2]:
        file.write(line + '\n')

# Finish writing the remaining 2 lines to the file
with open('output.txt', 'a') as file:
    for line in lines[2:]:
        file.write(line + '\n')
