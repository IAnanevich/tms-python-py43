# Дан список целых чисел. Подсчитать сколько четных чисел в списке.

number_list = [1, 2, 2, 3, 4, 5]
count_even = 0 

for i in number_list:
    if not i % 2:
        count_even += 1

print(f'Number of even numbers is: {count_even}')