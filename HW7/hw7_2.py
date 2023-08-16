# 1. Ввести с клавиатуры 4 строки и сохранить их в 4 разные переменные
# 2. Создать файл и записать в него первые 2 строки и закрыть файл
# 3. Затем открыть файл на редактирование и дозаписать оставшиеся 2 строки
# 4. В итоговом файле должны быть 4 строки, каждая из которых должна начинаться с новой строки

file_name = "hw7_2.txt"

# 1.Ввести с клавиатуры 4 строки и сохранить их в 4 разные переменные
print("\nPlease enter four string lines")
line_1 = input("First line >>")
line_2 = input("Second line >>")
line_3 = input("Third line >>")
line_4 = input("Fourth line >>")

# 2. Создать файл и записать в него первые 2 строки и закрыть файл
with open(file_name, "w") as some_file:
    some_file.write(line_1)
    some_file.write("\n")
    some_file.write(line_2)

# 3. Затем открыть файл на редактирование и дозаписать оставшиеся 2 строки
with open(file_name, "a") as some_file:
    some_file.write("\n")
    some_file.write(line_3)
    some_file.write("\n")
    some_file.write(line_4)

# 4. В итоговом файле должны быть 4 строки, каждая из которых должна начинаться с новой строки
with open(file_name, "r") as some_file:
    print("\nFile data:")
    some_file_data = some_file.read()
    print(some_file_data)
