"""2. Ввести с клавиатуры 4 строки и сохранить их в 4 разные переменные.
Создать файл и записать в него первые 2 строки и закрыть файл.
Затем открыть файл на редактирование и дозаписать оставшиеся 2 строки.
В итогом файле должны быть строки, каждая из которых должна начинаться с новой строки."""

string_1 = str(input('Enter first string: '))
string_2 = str(input('Enter second string: '))
string_3 = str(input('Enter third string: '))
string_4 = str(input('Enter fourth string: '))
f = open('nastya_hw7_2.txt', 'w')
f.write(string_1 + '\n')
f.write(string_2 + '\n')
f.close()
with open('nastya_hw7_2.txt', 'a') as f:
    f.write(string_3 + '\n')
    f.write(string_4 + '\n')
