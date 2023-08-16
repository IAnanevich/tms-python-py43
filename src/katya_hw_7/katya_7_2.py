str_1 = input("Введите строку 1:  ")
str_2 = input("Введите строку 2:  ")
str_3 = input("Введите строку 3:  ")
str_4 = input("Введите строку 4:  ")

f1 = open("katya_7_2.txt", "w")
f1.write(f"{str_1}\n{str_2}")
f1.close()

f2 = open("katya_7_2.txt", "a")
f2.write(f"\n{str_3}\n{str_4}")
f2.close()

print(open("katya_7_2.txt", "r").read())
