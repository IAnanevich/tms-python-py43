import sqlite3
from sqlite3 import Error


class SQLite3Client:
    DATABASE = "d:\\Program Files\\djangoProject\\db\\hw12.db"
    total_changes = 0
    last_row_id = 0

    def __init__(self) -> None:
        try:
            self.db = sqlite3.connect(database=self.DATABASE)
        except Error as e:
            print("error init", e)

    def query(self, query: str, params: tuple | None = ()) -> list[tuple] | None:
        cursor = self.db.cursor()
        self.total_changes = 0
        try:
            cursor.execute(query, params if params else None)
            self.db.commit()
            self.last_row_id = int(cursor.lastrowid)
            self.total_changes = int(self.db.total_changes)
            return cursor.fetchall()
        except Error as e:
            print("error query", e)
        finally:
            cursor.close()
        return None

    def __del__(self) -> None:
        if self.db:
            self.db.close()
