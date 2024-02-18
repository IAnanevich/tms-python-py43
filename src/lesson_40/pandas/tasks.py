import pandas as pd

# 1. Загрузите набор данных (например, CSV-файл) с информацией о фильмах или иных объектах.
# Используйте Pandas для чтения данных и выполните следующие задачи:
#     - Выведите общую информацию о DataFrame.
#     - Посчитайте количество уникальных значений в одном из столбцов.
#     - Найдите среднее значение числового столбца.


df = pd.read_csv('movies.csv')

print(df.info())
print()
print(df['Genre'].nunique())
print()
print(df['Rating'].mean())

# 2. Фильтрация и сортировка данных:
# Работайте с DataFrame, содержащим информацию о продажах товаров. Выполните следующие операции:
#     - Отфильтруйте данные по определенному критерию (например, продажи за определенный период).
#     - Отсортируйте DataFrame по значению одного из столбцов.
#     - Выведите топ-N записей в отсортированном DataFrame.

df = pd.read_csv('sales.csv')

print(df[df['Date'] > '2022-01-01'])
print()
sorted_df = df.sort_values('Sales')
print(sorted_df)
print()
print(sorted_df.head(2))

# 3. Используйте DataFrame с информацией о студентах и их оценках.
# Произведите группировку по категории и выполните следующие задачи:
#     - Найдите средний балл по каждой категории.
#     - Посчитайте количество студентов в каждой категории.
#     - Найдите максимальную оценку для каждой категории.

df = pd.read_csv('students.csv')

df_group_by_category = df.groupby('Category')['Score']

print(df_group_by_category.mean())
print()
print(df['Category'].value_counts())
print()
print(df_group_by_category.max())
