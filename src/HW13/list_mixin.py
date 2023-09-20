from models import Reader, Genre, Book, Order, engine
from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=engine)
session = Session()


def read_reader_table():
    readers = session.query(Reader).all()
    for i in readers:
        print(
            f'id: {i.pk}'
            f'f_name:{i.first_name}'
            f'l_name: {i.last_name}'
            f'email: {i.email}'
            f'{i.books}'
            f'{i.balance}',
            sep='\n'
        )


def read_book_table():
    books = session.query(Book).all()
    for i in books:
        print(
            f'id:{i.pk}'
            f'title: {i.title}'
            f'description: {i.description}'
            f'amount: {i.amount}'
            f'price: {i.price}',
            sep='\n'
        )


def read_genre_table():
    genres = session.query(Genre).all()
    for i in genres:
        print(
            f'id:{i.pk} '
            f'genre: {i.name}',
            sep='\n'
        )


def read_order_table():
    orders = session.query(Order).all()
    for i in orders:
        print(
            f'id: {i.pk}'
            f' reader: {i.user}'
            f' book: {i.book} ',
            sep="\n"
        )
