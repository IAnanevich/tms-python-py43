'''
Ввести предложение состоящее из двухслов. Поменять местами слова, добавить
восклицательный знак в начало и конец, слова разделить 3 символами(пробел
восклицательный знак и ещё пробел), вывести итоговое предложение на экран.
Задание необходимо выполнить 3-мя разными способами форматирования
'''

sentence = input('Enter a 2-word sentence').split(' ')

if len(sentence) == 2:
    print(f'!{sentence[1]} ! {sentence[0]}!')
    print("!{} ! {}!".format(sentence[1], sentence[0]))
    print("!{1} ! {0}!".format(*sentence))
    print("!%s ! %s!" % (sentence[1], sentence[0]))
else:
    print('The sentence was entered incorrectly!')
