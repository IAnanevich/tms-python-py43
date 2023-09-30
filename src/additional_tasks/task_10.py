# Дан список строк. Отформатировать все строки в формате {i}-{string}, где i это порядковый номер строки в списке.
# Использовать генератор списков. (можно использовать enumerate)

list_str = [
    "If thou wilt leave me, do not leave me last",
    "When other petty griefs have done their spite",
    "But in the onset come; so shall I taste",
    "At first the very worst of fortune's might",
    "And other strains of woe, which now seem woe",
    "Compared with loss of thee will not seem so",
]

list_str_new = [f"{i}-{list_str[i]}" for i in range(len(list_str))]
for st in list_str_new:
    print(st)
