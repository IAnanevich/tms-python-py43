# Ввести с клавиатуры 4 строки и сохранить их в 4 разные переменные.
# Cоздать файл и записать в него первые 2 строки и закрыть в файл.
# Затем открыть файл на редактирование и дозаписать оставшиеся 2 строки.
# В итогом файле должны быть 4 строки, каждая из которых должна начинаться с новой строки.

text1 = input(str("Enter text1 "))
text2 = input(str("Enter text2 "))
text3 = input(str("Enter text3 "))
text4 = input(str("Enter text4 "))

with open('file.txt', "w") as file:
    file.write(f'{text1}\n{text2}\n')
    file.close()
print(f'The first 2 lines are written: \n {text1} \n {text2}')
# Дозапись оставшихся 2 строк
with open('file.txt', "a") as file:
    file.write(f'{text3}\n{text4}\n')
    file.close()
print(f'The second 2 lines are written: \n {text3} \n {text4}')
