"""Дан произвольный список некоторых целых чисел, найдите значение 20 в нем и,
если оно присутствует, замените его на 200.
Обновите список только при первом вхождении числа 20"""

i = int(input('Enter the number of values is in the list: '))
j = []
for b in range(i):
    x = input('Enter a value into the list: ')
    j.append(x)
print(j)
if '20' in j:     # 2) добавь проверку на то, что может не быть элемента 20 в списке
    j[j.index('20')] = '200'  # 1) но можно было обойтись без remove и insert j[j.index(20)] = 200
    print(j)
else:
    print('There is no 20 on the list')
