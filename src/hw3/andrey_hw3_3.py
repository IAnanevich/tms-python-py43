'''
Написать программу которая получит имя и возраст пользователя, проверяет
возраст и выдаёт приветственное сообщение в зависимости от возраста :
- меньше нуля или ноль или не число “Ошибка повторите ввод”;
- больше нуля до 10 не включая “Привет шкет #Имя#”;
- от 10 до 18 включая “Как жизнь #Имя# ”;
- больше 10 и меньше 100 “Что желаете #Имя# ”;
- в противном случае “#Имя#, вы лжете - в наше время столько не живут ”;
Завернуть это в вечный цикл
'''
name = input('Enter name: ')
age = input('Enter age: ')

while not (age.isdigit() and (age := int(age)) and age > 0):
    age = input('Error: e-enter age: ')
if age < 10:
    print(f'Hello shket {name}')
elif age < 19:
    print(f'How are you {name}')
elif age < 100:
    print(f'whatever you want {name}')
else:
    print(f'{name}, you are lying nowadays in the Python language has the following form: they don\'t live so muc')
