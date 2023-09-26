from datetime import datetime

from sqlalchemy import create_engine, Column, Integer, String, Boolean, DateTime, SmallInteger, ForeignKey
from sqlalchemy.orm import sessionmaker, declarative_base, relationship

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


# O20 - one to one
# O2M - one to many / many to one
# M2M - many to many


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

    # o2o
    # books = relationship('Book')

    # o2m
    # books = relationship('Book', backref='user', uselist=False)

    # m2m
    groups = relationship('UserGroup', backref='user')


class Book(Base):
    __tablename__ = 'books'
    id = Column('id', Integer, primary_key=True, autoincrement=True)
    title = Column(String(100), nullable=False)
    copyright = Column(SmallInteger, nullable=False)

    # o2o
    # user_id = Column(Integer, ForeignKey('users.id'))

    # o2m
    user_id = Column(Integer, ForeignKey('users.id'))


# session.query(User).join(Book).all() - join

class UserGroup(Base):
    id = Column('id', Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    group_id = Column(Integer, ForeignKey('groups.id'))


class Group(Base):
    # m2m
    __tablename__ = 'groups'
    id = Column('id', Integer, primary_key=True, autoincrement=True)
    title = Column(String(100), nullable=False)
    users = relationship(UserGroup, backref='group')


class UserHandle:
    @staticmethod
    def read():
        return session.query(User).all()

    @staticmethod
    def get_by_id(pk: int) -> User:
        return session.query(User).get(ident=pk)

    @staticmethod
    def create(user: User):
        session.add(instance=user)
        session.commit()

    @classmethod
    def update(cls, pk: int, data: dict):
        obj = cls.get_by_id(pk=pk)

        for key, value in data.items():
            # obj.key = value
            # getattr(obj, key)
            setattr(obj, key, value)
        # obj.first_name = data
        session.add(obj)
        session.commit()
        # session.refresh(obj)
        # return obj

    @classmethod
    def delete(cls, pk: int):
        obj = cls.get_by_id(pk=pk)
        session.delete(obj)
        session.commit()


Base.metadata.create_all(engine)

user_handle = UserHandle()
# user_handle.create(user=User(
#     first_name='Ivan',
#     last_name='Ivanov',
#     email='ivan@gmail.com',
#     age=23
# ))
user_handle.update(pk=1, data={'first_name': 'Dima', 'age': 45})
users = user_handle.read()

print()
print()
print()

# print(users[0].email)
for i in users:
    print(i.first_name, i.id, i.age)
