# 3 |x|-|y|/1+|x*y|
x = int(input('Ввод x: '))  # текст в input
y = int(input('Ввод y: '))
print(f'|{x}|-|{y}|/1+|{x}*{y}|= {abs(x)-abs(y)/1+abs(x*y)}')
