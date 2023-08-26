# В заданной строке расположить в обратном порядке все слова.
# Разделителями слов считаются пробелы.
# сделать используя .split()

some_string = "В заданной строке расположить в обратном порядке все слова"
splits = some_string.split()
splits = splits[::-1]

new_string = str()
for word in splits:
    new_string += word + " "

print("\n")
print(some_string)
print(new_string)
