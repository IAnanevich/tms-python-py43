# Написат декоратор который бы считал и выводил время выполнения.


def pow3_func(x: float | str) -> float | None:
    try:
        r = x**3
        print(f" {x}^3 = {r}")
        return r
    except Exception as error:
        print(error)
        return None


pow3_func(5)
pow3_func("5")
