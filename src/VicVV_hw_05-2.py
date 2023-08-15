# 2. Написать программу для нахождения факториала. Рекурсивной функцией

def factor(n: int) -> int:
    while n > 1:
        return factor(n-1) * n
    else:
        return 1


f = 64
print(f"факториал {f} = {factor(f)}")
