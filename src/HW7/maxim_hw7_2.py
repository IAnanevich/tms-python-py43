# Ввести с клавиатуры 4 строки и сохранить их в 4 разные переменные. Создать
# файл и записать в него первые 2 строки и закрыть файл. Затем открыть файл на
# редактирование и дозаписать оставшиеся 2 строки. В итоговом файле должны быть 4
# строки, каждая из которых должна начинаться с новой строки.

if __name__ == "__main__":
    text_input = "Enter a string: "
    str_1, str_2, str_3, str_4 = input(text_input), input(text_input), input(text_input), input(text_input)
    with open('temp.txt', 'w', encoding='utf-8') as file:
        print(str_1, str_2, sep="\n", file=file)
    with open('temp.txt', 'a') as file:
        file.write(f'{str_3}\n{str_4}')
