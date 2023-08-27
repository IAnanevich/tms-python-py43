# Имеется текстовый файл. Все четные строки этого файла записать во второй файл, а нечетные — в третий файл.
# Порядок следования строк сохраняется.

with open('even_not_even.txt') as f:
    data_file = f.readlines()
    res = ''
    mres = ''
    with open('even_string.txt', 'w') as file_even:
        for i in range(len(data_file)):
            if i % 2 != 0:
                res += data_file[i]
                file_even.write(res)
            else:
                with open('not_even_string.txt', 'w') as file_not_even:
                    mres += data_file[i]
                    file_not_even.write(mres)
