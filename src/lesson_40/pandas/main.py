# import pandas as pd
# import numpy as np


# anime = pd.read_csv('anime.csv')
# rating = pd.read_csv('rating.csv')
# anime_modified = anime.set_index('name')

# print(anime)
# print(rating)

# df = pd.DataFrame(
#     [
#         [1, 'Andrew', 17],
#         [2, 'Petr', 23],
#         [3, 'Artem', 56]
#     ],
#     columns=['id', 'name', 'age']
# )
# print(df)
# df_copy = df.copy(deep=True)
# print(df_copy)

# print(anime.head(5))
# print(20*'-')
# print(anime.tail(2))
# print(list(anime.columns))
# print(anime['type'])
# print(len(anime))
#
# print(len(rating['user_id'].unique()))

# print(anime.info())
# print(anime.dtypes)

# print(anime.describe())

# print(anime['genre'].tolist())
# print(anime['genre'])

# print(anime.columns.tolist())

# anime['is_true'] = anime['anime_id'] % 10 != 0
# print(anime.head(20))

# new_anime = anime[['name', 'episodes']]
# print(new_anime)

# print(anime.drop(['anime_id', 'genre', 'members'], axis=1).head())

# df1 = anime[10:12]
# df2 = anime[12:14]
# df3 = pd.concat([df1, df2], ignore_index=True)
# print(df3)

# print(anime_modified.loc['Under World'])
# print(anime.iloc[100:120])

# print(anime[anime['rating'] < 3])

# print(anime.groupby('type').count())

# print(anime.sort_values('rating', ascending=False))
