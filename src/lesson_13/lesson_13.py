from datetime import datetime

from sqlalchemy import create_engine, Column, Integer, String, Boolean, DateTime
from sqlalchemy.orm import sessionmaker, declarative_base

engine = create_engine('sqlite:///test.db', echo=True)

# Подключение к серверу MySQL на localhost с помощью PyMySQL DBAPI.
# engine = create_engine("mysql+pymysql://root:pass@localhost/mydb")
# Подключение к серверу MySQL по ip 23.92.23.113 с использованием mysql-python DBAPI.
# engine = create_engine("mysql+mysqldb://root:pass@23.92.23.113/mydb")
# Подключение к серверу PostgreSQL на localhost с помощью psycopg2 DBAPI
# engine = create_engine("postgresql+psycopg2://root:pass@localhost/mydb")
# Подключение к серверу Oracle на локальном хосте с помощью cx-Oracle DBAPI.
# engine = create_engine("oracle+cx_oracle://root:pass@localhost/mydb"))
# Подключение к MSSQL серверу на localhost с помощью PyODBC DBAPI.
# engine = create_engine("oracle+pyodbc://root:pass@localhost/mydb")

# session = Session(bind=engine)
Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()


class User(Base):  # model
    __tablename__ = 'users'
    id = Column('id', Integer, primary_key=True, autoincrement=True)
    first_name = Column(String(20), nullable=False)
    last_name = Column(String(20), nullable=False)
    email = Column(String(20), nullable=False, unique=True)
    age = Column(Integer)
    is_admin = Column(Boolean, nullable=False, default=False)
    created_at = Column(DateTime(), default=datetime.now)
    updated_at = Column(DateTime(), default=datetime.now, onupdate=datetime.now)


class UserHandle:
    def __init__(self) -> None:
        pass

    @staticmethod
    def read():
        return session.query(User).all()

    @staticmethod
    def create(user: User):
        session.add(instance=user)
        session.commit()


Base.metadata.create_all(engine)

user_handle = UserHandle()
# user_handle.create(user=User(
#     first_name='Petr',
#     last_name='Petrov',
#     email='petr1@gmail.com',
#     age=23
# ))
users = user_handle.read()
for i in users:
    print(i.last_name)
