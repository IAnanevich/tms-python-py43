# NoSQL

# [{id: 1, name: 'Petr'}, {id: 2, name: Alex}] - key-value NoSQL DB (Redis)
# документориентированные - NoSQL (MondoDB)
# колоночные - NoSQL (Cassandra)
# графовые - NoSQL


import sqlite3


def connect_to_session(path: str) -> sqlite3.Connection:
    try:
        return sqlite3.connect(database=path)
    except sqlite3.Error as error:
        print(error)


class SQLite3Client:
    def __init__(self, session: sqlite3.Connection) -> None:
        self.session = session

    def execute_query(self, query: str) -> None:
        cursor = self.session.cursor()
        try:
            cursor.execute(query)
            self.session.commit()
        except sqlite3.Error as error:
            print(error)

    def execute_read_query(self, query: str) -> list[tuple]:
        cursor = self.session.cursor()
        try:
            cursor.execute(query)
            return cursor.fetchall()
        except sqlite3.Error as error:
            print(error)


client = SQLite3Client(session=connect_to_session(path='src/lesson_12/sqlite3.sqlite'))  # "E:\\sm_app.sqlite"
create_table_users = """
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(20) NOT NULL,
    age INTEGER,
    gender VARCHAR(20),
    nationality VARCHAR(20)
)
"""
client.execute_query(query=create_table_users)
create_users = """
INSERT INTO 
    users (name, age, gender, nationality)
VALUES 
    ('Alena', 23, 'female', 'USE')
"""
# client.execute_query(query=create_users)
get_users = """
SELECT * FROM users 
"""
users = client.execute_read_query(query=get_users)
for user in users:
    print(user)


# Get, Retrieve, Create, Update, Delete
# Users.objects.all() = SELECT * FROM Users - Django ORM
# session.add(table(field1, field2 ...)) - SQLAlchemy

# ACID
# A - атомарность - транзакция 100% завершена или 100% откачена назад
# C - согласованность - все данные в одном формате (согласованы типы)
# I - изолированность - транзакции выполняются в изолированной среде
# D - надежность - упал сервер -> выполненная транзакция осталась

# CAP теорема
# C - согласованность - допустимые данные зафиксированы и готовы чтению
# A - доступность - любой запрос к бд завершается корректным образом
# P - устойчивость к разделению системы - возможность распределить нагрузку
# Кейс “позвони-напомним”
# 1. Мне начинают звонить клиенты с просьбой что-то записать, чтобы потом можно
# было уточнить (напомнить им)
# 2. Я беру ручку и блокнот и пишу все их требования
# (делаю один= − РАЗДЕЛЯЕМОСТЬ)
# 3.  Поступает очень много звонков и я уже не справляюсь с нагрузкой
# (не отвечаю на все запросы= − ДОСТУПНОСТЬ)
# 4. Прошу жену и мы записываем все в свои блокноты.
# 5.  Ко мне пришел запрос записать, к жене - напомнить.
# (жена не знает что надо напомнить= − СОГЛАСОВАННОСТЬ)
# 6. Решили дублировать все запросы в оба блокнота
# 7. Перестаем успевать дублировать данные ;)))
# (не отвечаю на все запросы= − ДОСТУПНОСТЬ)