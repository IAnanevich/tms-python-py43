import sqlalchemy as sa
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy.orm import sessionmaker
from base_model import BaseModel

engine = create_engine('sqlite:///bookshop.db', echo=True)
Session = sessionmaker(bind=engine)
Base = declarative_base()
session = Session()


class Reader(BaseModel):
    __tablename__ = 'readers'
    first_name = sa.Column('First Name', sa.String(20), nullable=False)
    last_name = sa.Column('Last Name', sa.String(30), nullable=False)
    email = sa.Column('Email Address', sa.String(20), nullable=False, unique=True)
    age = sa.Column('Age', sa.Integer, nullable=False)
    balance = sa.Column('Balance', sa.Integer, nullable=False)
    books = relationship('Book', backref='reader', uselist=False)


class Book(BaseModel):
    __tablename__ = 'books'
    title = sa.Column('Book title', sa.String(20), nullable=False)
    description = sa.Column('Book description', sa.Text, nullable=False)
    amount = sa.Column('Book amount', sa.Integer, nullable=False)
    price = sa.Column('Book price', sa.Float, nullable=False)
    genre_id = sa.Column('genre id', sa.Integer, sa.ForeignKey('genre.id'))

    genre = relationship('genres', backref='genre_id', lazy=True)


class Order(BaseModel):
    __tablename__ = 'orders'
    book_id = sa.Column('book id', sa.Integer, sa.ForeignKey('books.id'))
    user_id = sa.Column('reader id', sa.Integer, sa.ForeignKey('readers.id'))

    user = relationship("Reader", backref='user_id', lazy=True)
    book = relationship("Books", backref='book_id', lazy=True)


class Genre(BaseModel):
    __tablename__ = 'genres'
    name = sa.Column('genre name', sa.String(20), nullable=False)


Base.metadata.create_all(bind=engine)
