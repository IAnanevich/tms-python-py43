# Дан список. Создать новый список, сдвинутый на 1 элемент влево

spisok = [1, 2, 3, 9, -90, 79, 4, 5]

n = 0
spisok_new = []
a1 = spisok.pop(0)

while n < len(spisok):
    spisok_new.insert((n), spisok[n])
    n += 1

spisok_new.append(a1)
print(spisok_new)

