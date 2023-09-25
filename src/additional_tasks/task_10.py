# Дан список строк. Отформатировать все строки в формате {i}-{string},
# где i это порядковый номер строки в списке.
# Использовать генератор списков. (можно использовать enumerate)

s = input()

stringer = s.split()[0::]
for i in enumerate(stringer):
    print(f'{i}')
    # print(i)
