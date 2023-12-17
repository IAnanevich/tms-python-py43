# Ввести предложение, состоящее из 2 слов. Поменять местами слова, добавить восклицательный знак в начало и конец,
# слова разделить 3 символами(пробел, восклицательны знак и еще пробел), вывести итоговое предложение на экран.
# Задание необходимо выполнить 3-мя разными способами форматирования.

# my_text = input('Enter sentence from 2 words:')
my_text = 'Hello world'
first_word = my_text.split()[0]
second_word = my_text.split()[1]

print(f'!{second_word} ! {first_word}!')
print('!{} ! {}!'.format(second_word, first_word))
print('!{1} ! {0}!'.format(first_word, second_word))
print('!', second_word, ' ! ', first_word, '!', sep='')
