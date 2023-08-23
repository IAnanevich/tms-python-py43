# Прочитать сохранённый json-файл и записать данные на диск в csv-файл,
# первой строкой которого озаглавив каждый столбец и добавив новый столбец 'телефон'.
import pandas as pd

if __name__ == "__main__":
    with open('example.csv', 'r', newline='') as file_csv:
        df = pd.read_csv(file_csv, dtype='str',)
        df.pop('Age')
        columns = {i: f'Person {i + 1}' for i in range(len(df.index))}
        df.rename(index=columns, inplace=True)
        df = df.T
        try:
            with pd.ExcelWriter("example.xlsx", mode='w') as writer:
                df.to_excel(writer, )   # TODO: выравнивание по центру не нашёл для pandas
        except ValueError as e:
            print(e)
