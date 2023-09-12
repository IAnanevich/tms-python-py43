from SQLite3Client import SQLite3Client


class Product(SQLite3Client):
    table = "product"

    def __init__(self) -> None:
        super().__init__()

    # TODO упрощенный вариант метода. добавить !, >, >=, <, <=, в key в начало. они будут служить флагом как
    # фильтровать.
    def get_list(self, filter: dict) -> list[tuple] | None:
        pre_filter = []
        for key, value in filter.items():
            if isinstance(value, list):
                pre_filter.append(f"{key} IN ('" + "','".join(list) + ")'")
            else:
                pre_filter.append(f"{key} = '{value}'")
        sql = f"SELECT * FROM {self.table}"
        if pre_filter:
            sql += f" WHERE {' AND '.join(pre_filter)}"
        return self.query(sql)

    def insert(self, params: dict) -> bool | int:
        # конструкция получилась дикой) хотел чтоб более универсально было
        self.query(
            f"INSERT INTO {self.table} {tuple(params.keys())} VALUES({','.join(['?' for _ in range(len(params))])})",
            tuple(params.values()))

        if self.last_row_id > 0:
            return self.last_row_id
        return False

    def update(self, id: int, params: dict) -> bool:
        update_values = ','.join(list(f"{key}='{value}'" for (key, value) in params.items()))
        self.query(f"UPDATE {self.table} SET {update_values} WHERE id = ?", (id,))
        if self.total_changes == 1:
            return True
        return False

    def delete(self, id: int) -> bool:
        self.query(f"DELETE FROM {self.table} WHERE id = ?", (id,))
        if self.total_changes == 1:
            return True
        return False

    def create(self) -> None:
        query = f"""
            CREATE TABLE IF NOT EXISTS `{self.table}` (
              id INTEGER PRIMARY KEY AUTOINCREMENT,
              name VARCHAR(50) NOT NULL,
              price DECIMAL(18,4) NOT NULL,
              quantity INTEGER(8) NOT NULL,
              comment TEXT(300) NOT NULL
            )
        """
        self.query(query)
