# Ввести предложение состоящее из двух слов.  Поменять местами слова...
# fraza = input('Enter 2 words: ')
fraza = "hello VicVV rrrf ffff w ffff frrrr"
words = fraza.split()
if len(words) != 2:
    print(f'надо 2 слова, а не { len(words)}')
else:
    print(f'v.1: !{words[1]} ! {words[0]}!')
    print('v.2: !%s ! %s!' % (words[1], words[0]))
    print('v.3: !{} ! {}!'.format(words[1], words[0]))
