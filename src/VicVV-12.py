import sqlite3


class SQLclient:
    def __init__(self, session: sqlite3.Connection):
        self.session = session

    def create(self, q: str) -> None:
        cursor = self.session.cursor()
        try:
            cursor.execute(q)
            self.session.commit()
            print("create - ok")
        except sqlite3.Error as err:
            print(err)

    def read(self, table_name: str, cond: str = "True"):
        cursor = self.session.cursor()
        try:
            cursor.execute(f"select * from {table_name} where {cond}")
            return cursor.fetchall()
        except sqlite3.Error as err:
            print(err)

    def update(self, table_name: str, field: dict, cond: str = "True"):
        cursor = self.session.cursor()
        try:
            f_ = "*"
            for k, v in field.items():
                f__ = f", {k} = {v} "
                f_ = f_ + f__
            f_ = f_.replace("*,", "")
            q = f"update {table_name} set {f_} where {cond}"
            print(q)
            cursor.execute(q)
            self.session.commit()
        except sqlite3.Error as err:
            print(err)

    def insert(self, table_name: str, field: dict):
        cursor = self.session.cursor()
        try:
            f_ = "*"
            v_ = "*"
            for k, v in field.items():
                f__ = f", {k} "
                f_ = f_ + f__
                v__ = f", {v} "
                v_ = v_ + v__

            f_ = f_.replace("*,", "")
            v_ = v_.replace("*,", "")
            q = f"insert into {table_name} ({f_}) values ( {v_} )"
            print(q)
            cursor.execute(q)
            self.session.commit()
        except sqlite3.Error as err:
            print(err)


def create_table(sql_: SQLclient):
    q = """create table if not exists 
    Goods (id integer Primary Key Autoincrement, 
            name Varchar(100),
            price real,
            quantity real,
            comment text
            )"""
    sql_.create(q)


sql = SQLclient(session=sqlite3.Connection("./mySqlBase.sqlite"))
while True:
    f = input("Что делаем? (C, R, U, D, I, exit): ")
    if f.upper() == "C":
        create_table(sql)
    elif f.upper() == "R":
        resp = sql.read("Goods")
        if resp:
            for line_ in resp:
                print(line_)
        else:
            print("empty")
    elif f.upper() == "U":
        id_ = input("id строки для изменения? : ")
        k_ = ["name", "price", "quantity", "comment"]
        val_ = {}
        for key in k_:
            val = input(f"{key} = ")
            val_[key] = f'"{val}"'

        sql.update(table_name="Goods", field=val_, cond=f"id = {id_}")
    elif f.upper() == "I":
        k_ = ["name", "price", "quantity", "comment"]
        val_ = {}
        for key in k_:
            val = input(f"{key} = ")
            val_[key] = f'"{val}"'

        sql.insert(table_name="Goods", field=val_)

    elif f.upper() == "D":
        print(sql.read("Goods"))
    else:
        break
