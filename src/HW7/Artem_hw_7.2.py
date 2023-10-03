#Ввести с калвы 4 строки и сохранить их в 4 разные переменные
#создать файл и записать в него превые две строки и закрыть
#открыть файл на рдактирование и дозаписать ост две строки

line_1 = str(input("Enter first line: "))
line_2 = str(input("Enter second line: "))
line_3 = str(input("Enter third line: "))
line_4 = str(input("Enter fourth line: "))

with open('lines.txt', 'w') as f:
    f.write(f'{line_1} \n')
    f.write(f'{line_2} \n')

with open('lines.txt', 'a') as f:
    f.write(f'{line_3} \n')
    f.write(f'{line_4} \n')
