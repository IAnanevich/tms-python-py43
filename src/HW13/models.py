from datetime import datetime
import sqlalchemy as sa
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy.orm import sessionmaker
from base_model import BaseModel

# from base_model import BaseModel

engine = create_engine('sqlite:///bookshop.db', echo=True)
# session = Session(bind=engine)
Session = sessionmaker(bind=engine)  # metaclass
Base = declarative_base()
session = Session()


# Base.metadata.create_all(bind=engine)


class Reader(BaseModel):
    __tablename__ = 'readers'
    pk = sa.Column('id', sa.Integer, primary_key=True, autoincrement=True)
    first_name = sa.Column('First Name', sa.String(20), nullable=False)
    last_name = sa.Column('Last Name', sa.String(30), nullable=False)
    email = sa.Column('Email Address', sa.String(20), nullable=False, unique=True)
    age = sa.Column('Age', sa.Integer, nullable=False)
    balance = sa.Column('Balance', sa.Integer, nullable=False)
    # created_at = sa.Column('Created time', sa.DateTime(), default=datetime.now)
    # update_at = sa.Column('Update time', sa.DateTime(), default=datetime.now, onupdate=datetime.now)
    books = relationship('Book', backref='reader', uselist=False)


class Book(BaseModel):
    __tablename__ = 'books'
    pk = sa.Column('id', sa.Integer, primary_key=True, autoincrement=True)
    title = sa.Column('Book title', sa.String(20), nullable=False)
    description = sa.Column('Book description', sa.Text, nullable=False)
    amount = sa.Column('Book amount', sa.Integer, nullable=False)
    price = sa.Column('Book price', sa.Float, nullable=False)
    genre_id = sa.Column('genre id', sa.Integer, sa.ForeignKey('genre.id'))  # attantion
    # created_at = sa.Column('Created time', sa.DateTime(), default=datetime.now)
    # update_at = sa.Column('Update time', sa.DateTime(), default=datetime.now, onupdate=datetime.now)
    genre = relationship('genres', backref='genre_id', lazy=True)  # у одной книги много жанров


class Order(BaseModel):
    __tablename__ = 'orders'
    pk = sa.Column('id', sa.Integer, primary_key=True, autoincrement=True)
    book_id = sa.Column('book id', sa.Integer, sa.ForeignKey('books.id'))
    user_id = sa.Column('reader id', sa.Integer, sa.ForeignKey('readers.id'))  # JOIN
    # created_at = sa.Column('Created time', sa.DateTime(), default=datetime.now)
    # update_at = sa.Column('Update time', sa.DateTime(), default=datetime.now, onupdate=datetime.now)
    user = relationship("Reader", backref='user_id', lazy=True)
    book = relationship("Books", backref='book_id', lazy=True)


class Genre(BaseModel):
    __tablename__ = 'genres'
    pk = sa.Column('id', sa.Integer, primary_key=True, autoincrement=True)
    name = sa.Column('genre name', sa.String(20), nullable=False)
    # created_at = sa.Column('Created time', sa.DateTime(), default=datetime.now)
    # update_at = sa.Column('Update time', sa.DateTime(), default=datetime.now, onupdate=datetime.now)


Base.metadata.create_all(bind=engine)
