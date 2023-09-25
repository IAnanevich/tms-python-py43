# Описать функцию fact2( n ), вычисляющую двойной факториал :
# n!! = 1·3·5·...·n, если n — нечетное;
# n!! = 2·4·6·...·n, если n — четное (n > 0 — параметр целого типа).

n = int(input("Введите n: "))
num = 0
if n % 2:
    num = 1
else:
    num = 2
for i in range(num, n + 2, 2):
    num *= i
    print(f'{i}',end=' ')
print(f'fact2 = {num}')
