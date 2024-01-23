# В конец существующего текстового файла записать три
# новые строки текста. Записываемые строки вводятся с клавиатуры.

str_7 = input("Введите строку 7:  ")
str_8 = input("Введите строку 8:  ")
str_9 = input("Введите строку 9:  ")

f2 = open(
    "/Users/katsiarynamakaranka/Desktop/pythonProject1/tms-python-py43/src/additional_tasks/task_13/task_13.txt", "a"
)
f2.write(f"\n{str_7}\n{str_8}\n{str_9}")
f2.close()
