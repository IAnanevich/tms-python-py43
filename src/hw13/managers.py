from sqlalchemy.orm import Session
from models import Person, Book, Order, Genre

class UserManager:
    def __init__(self, session: Session):
        self.session = session

    def create_person(self, first_name, last_name, email, age, balance):
        person = Person(first_name=first_name, last_name=last_name, email=email, age=age, balance=balance)
        self.session.add(person)
        self.session.commit()
        return person

    def update_balance(self, person_id, new_balance):
        person = self.session.query(Person).filter_by(id=person_id).first()
        if person:
            person.balance = new_balance
            self.session.commit()

    def get_all_people(self):
        return self.session.query(Person).all()

    def get_person_by_id(self, person_id):
        return self.session.query(Person).filter_by(id=person_id).first()

    def delete_person(self, person_id):
        person = self.session.query(Person).filter_by(id=person_id).first()
        if person:
            self.session.delete(person)
            self.session.commit()

class BookManager:
    def __init__(self, session: Session):
        self.session = session

    def create_book(self, title, description, amount, price, genre_id):
        book = Book(title=title, description=description, amount=amount, price=price, genre_id=genre_id)
        self.session.add(book)
        self.session.commit()
        return book

    def update_book_quantity(self, book_id, new_quantity):
        book = self.session.query(Book).filter_by(id=book_id).first()
        if book:
            book.amount = new_quantity
            self.session.commit()

    def get_all_books(self):
        return self.session.query(Book).all()

    def get_book_by_id(self, book_id):
        return self.session.query(Book).filter_by(id=book_id).first()

    def delete_book(self, book_id):
        book = self.session.query(Book).filter_by(id=book_id).first()
        if book:
            self.session.delete(book)
            self.session.commit()

class OrderManager:
    def __init__(self, session: Session):
        self.session = session

    def create_order(self, title_id, user_id):
        order = Order(title_id=title_id, user_id=user_id)
        self.session.add(order)
        self.session.commit()
        return order

    def get_all_orders(self):
        return self.session.query(Order).all()

    def get_order_by_id(self, order_id):
        return self.session.query(Order).filter_by(id=order_id).first()

    def delete_order(self, order_id):
        order = self.session.query(Order).filter_by(id=order_id).first()
        if order:
            self.session.delete(order)
            self.session.commit()

class GenreManager:
    def __init__(self, session: Session):
        self.session = session

    def create_genre(self, name):
        genre = Genre(name=name)
        self.session.add(genre)
        self.session.commit()
        return genre

    def get_all_genres(self):
        return self.session.query(Genre).all()

    def get_genre_by_id(self, genre_id):
        return self.session.query(Genre).filter_by(id=genre_id).first()

    def delete_genre(self, genre_id):
        genre = self.session.query(Genre).filter_by(id=genre_id).first()
        if genre:
            self.session.delete(genre)
            self.session.commit()