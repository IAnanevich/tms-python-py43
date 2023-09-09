# Ввести с клавиатуры 4 строки и сохранить их в 4 разные переменные.
# Создать файли записать в него первые 2 строки и закрыть файл.
# Затем открыть файл на редактирование и дописать оставшиеся 2 строки.
# В итоговом файле должны быть 4 строки, каждая из которых должна начинаться с новой строки.

line_1 = input("Enter first string: ")
line_2 = input("Enter second string: ")
line_3 = input("Enter third string: ")
line_4 = input("Enter fourth string: ")

# открываем файл или создаем новый для записи, пишем 2 строки
with open("marina_hw7_2.txt", "w") as file:
    file.write(f"{line_1}\n{line_2}\n")
# открываем файл для продолжения записи, пишем оставшиеся 2 строки
with open("marina_hw7_2.txt", "a") as file:
    file.write(f"{line_3}\n{line_4}\n")
