from sqlalchemy import create_engine, Column, Integer, String, Float, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime

engine = create_engine('sqlite:///nya.db', echo=True)
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()


class BaseModel(Base):
    id = Column(Integer, primary_key=True, autoincrement=True)
    created_at = Column(DateTime(), default=datetime.now)
    updated_at = Column(DateTime(), default=datetime.now, onupdate=datetime.now)


class Human(BaseModel):
    __tablename__ = 'humans'
    first_name = Column(String(20), nullable=False)
    last_name = Column(String(20), nullable=False)
    email = Column(String(20), unique=True)
    age = Column(Integer)
    balance = Column(Float)


class Book(BaseModel):
    __tablename__ = 'books'
    title = Column(String(20))
    description = Column()
    amount = Column(Integer)
    price = Column(Float)
    genre_id = Column(Integer)


class Order(BaseModel):
    __tablename__ = 'orders'
    title_id = Column(Integer, unique=True)
    user_id = Column(Integer, primary_key=True, autoincrement=True)


class Genre(BaseModel):
    __tablename__ = 'genres'
    name = Column(String(20))


class ListMixin:
    def list(self, session):
        return session.query(self).all()


class CreateMixin:
    def create(self, session):
        session.add(self)
        session.commit()


class UpdateMixin:
    def update(self, session):
        pass


class DeleteMixin:
    def delete(self, session):
        session.delete(self)
        session.commit()


class UserManager(ListMixin, CreateMixin, UpdateMixin, DeleteMixin):
    pass


class BookManager(ListMixin, CreateMixin, UpdateMixin, DeleteMixin):
    pass


class OrderManager(ListMixin, CreateMixin, UpdateMixin, DeleteMixin):
    pass


class GenreManager(ListMixin, CreateMixin, UpdateMixin, DeleteMixin):
    pass


while True:
    print("Menu:")
    print("[1] Create")
    print("[2] Add")
    print("[3] Read")
    print("[4] Modify")
    print("[5] Delete")
    print("[0] Exit")
    try:
        choice = input("Enter your choice: ")
        if choice == 0:
            break
        elif choice == 1:
            pass
        elif choice == 2:
            while True:
                print("Menu:")
                print("[1] Add a user")
                print("[2] Add a book")
                print("[3] Add a genre")
                print("[0] Go back")
                try:
                    new_choice = input("Enter your choice: ")
                    if new_choice == 0:
                        break
                except Exception as e:
                    print(e)
        elif choice == 3:
            while True:
                print("Menu:")
                print("[1] View users")
                print("[2] View books")
                print("[3] View orders")
                print("[4] View genres")
                print("[0] Go back")
                try:
                    new_choice = input("Enter your choice: ")
                    if new_choice == 0:
                        break
                except Exception as e:
                    print(e)
        elif choice == 4:
            while True:
                print("Menu:")
                print("[1] Change user ")
                print("[2] Change book")
                print("[3] Change genre")
                print("[0] Go back")
                try:
                    new_choice = input("Enter your choice: ")
                    if new_choice == 0:
                        break
                except Exception as e:
                    print(e)
        elif choice == 5:
            while True:
                print("Menu:")
                print("[1] Delete the user")
                print("[2] Delete book")
                print("[3] Delete genre")
                print("[0] Go back")
                try:
                    new_choice = input("Enter your choice: ")
                    if new_choice == 0:
                        break
                except Exception as e:
                    print(e)
    except Exception as e:
        print(e)
