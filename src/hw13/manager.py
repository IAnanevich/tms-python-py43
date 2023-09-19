from datetime import datetime
from sqlalchemy.exc import IntegrityError

from models import User, Order, Book, Genre
from database import session
from helpers import Helpers
import config


class BaseManager:
    last_error = ""

    def __init__(self):
        self.entity = None

    def list(self, filter: list | None = None, limit: int | None = None, page: int | None = 0) -> list:
        query = session.query(self.entity)
        if limit is not None and limit > 0:
            query = query.limit(limit)
        if page is not None and page > 1:
            query = query.offset((page - 1) * config.LIMIT_ITEM_PAGE)
        if filter is not None:
            query = query.filter(filter)

        return query.all()

    def _save(self, obj: object) -> None:
        try:
            session.add(obj)
            session.flush()
            session.commit()
        except IntegrityError as e:
            print(e)
            Helpers.print_color("Возврат назад...", "red")
            session.rollback()
            Helpers.print_color("Транзакция не удалась.", "red")

    def _delete(self, pk: int) -> None:
        try:
            obj = self.get_by_id(pk=pk)
            if obj is not None:
                session.delete(obj)
                session.commit()
        except IntegrityError as e:
            print(e)
            Helpers.print_color("Возврат назад...", "red")
            session.rollback()
            Helpers.print_color("Транзакция не удалась.", "red")

    def get_by_id(self, pk: int):
        # return session.query(self.entity).get(ident=pk)  # ругается на deprecated. еще глянуть потом
        return session.query(self.entity).filter_by(id=pk).scalar()


class UserManager(BaseManager):
    def __init__(self):
        super().__init__()
        self.entity = User

    def add(self, params: dict) -> int | bool:
        email = Helpers.htmlspecialchars(params["email"])
        if not Helpers.validate_email(email):
            self.last_error = "Введенный емейл невалиден"
            return False

        # проверяем нет ли уже такого пользователя по еймейл
        res = session.query(self.entity).filter_by(email=email).scalar()
        if res is not None:
            self.last_error = f"Email уже используется c ID = {res.id}"
            return False

        first_name = Helpers.htmlspecialchars(params["first_name"])
        last_name = Helpers.htmlspecialchars(params["last_name"])
        if len(first_name) < 3 or len(last_name) < 3:
            self.last_error = "Введите имя и фамилию"
            return False

        try:
            age = int(Helpers.htmlspecialchars(params["age"]))
        except ValueError:
            age = None

        try:
            balance = float(Helpers.htmlspecialchars(params["balance"]))
        except ValueError:
            balance = 0

        user = self.entity(
            first_name=first_name,
            last_name=last_name,
            email=email,
            age=age,
            balance=balance
        )

        self._save(user)  # Add the user

        if user.id is not None:
            return user.id
        return False

    def update(self, id: int, params: dict) -> None | bool:
        user = self.get_by_id(pk=id)
        if user is None:
            self.last_error = f"Пользователь {id} не найден"
            return False

        email = Helpers.htmlspecialchars(params["email"])
        if len(email) > 0:
            if not Helpers.validate_email(email):
                self.last_error = "Введенный емейл невалиден"
                return False

            # проверяем нет ли уже такого еймейла у другого пользователя
            res = session.query(User).filter(User.id != id, User.email == email).scalar()
            if res is not None:
                self.last_error = f"Email используется у другого пользователя c ID = '{res.id}'"
                return False

        first_name = Helpers.htmlspecialchars(params["first_name"])
        last_name = Helpers.htmlspecialchars(params["last_name"])
        age = Helpers.htmlspecialchars(params["age"])
        balance = Helpers.htmlspecialchars(params["balance"])

        if len(first_name) > 0:
            user.first_name = first_name
        if len(last_name) > 0:
            user.last_name = last_name
        if len(email) > 0:
            user.email = email
        if len(age) > 0:
            try:
                user.age = int(age)
            except ValueError:
                pass
        if len(balance) > 0:
            try:
                user.balance = float(balance)
            except ValueError:
                pass

        user.updated_at = datetime.now()
        self._save(user)  # Update the user

        return False

    def remove(self, pk):
        # смотрим нет ли заказов у этого пользователя. Если есть возвращаем ошибку и id первого заказов
        order = session.query(Order).filter_by(user_id=pk).first()
        if order is not None:
            Helpers.print_color(f"Ошибка удаления. У пользователя есть активные заказы. {order.id}", "red")
            return False
        self._delete(pk=pk)


class BookManager(BaseManager):
    def __init__(self):
        super().__init__()
        self.entity = Book

    def add(self, params: dict) -> int | bool:

        name = Helpers.htmlspecialchars(params["name"])
        if len(name) <= 3:
            self.last_error = "Введите название книги"
            return False

        description = Helpers.htmlspecialchars(params["description"])

        try:
            amount = int(params["amount"])
        except ValueError:
            amount = 0

        try:
            price = float(params["price"])
        except ValueError:
            price = 0

        try:
            genre_id = int(params["genre_id"])
            if session.query(Genre).filter_by(id=genre_id).scalar() is None:
                genre_id = None
        except ValueError:
            genre_id = None

        book = self.entity(
            name=name,
            description=description,
            amount=amount,
            price=price,
            genre_id=genre_id
        )

        self._save(book)  # Add book

        if book.id is not None:
            return book.id
        return False

    def update(self, id: int, params: dict) -> None | bool:
        book = self.get_by_id(pk=id)
        if book is None:
            self.last_error = f"Книга {id} не найдена"
            return False

        if len(params["name"]) > 3:
            book.name = Helpers.htmlspecialchars(params["name"])
        if len(params["description"]) > 0:
            book.description = Helpers.htmlspecialchars(params["description"])

        if len(params["amount"]) > 0:
            try:
                book.amount = int(params["amount"])
            except ValueError:
                pass

        if len(params["price"]) > 0:
            try:
                book.price = float(params["price"])
            except ValueError:
                pass

        if len(params["genre_id"]) > 0:
            try:
                genre_id = int(params["genre_id"])
                if session.query(Genre).filter_by(id=genre_id).scalar() is not None:
                    book.genre_id = genre_id
            except ValueError:
                book.genre_id = None

        book.updated_at = datetime.now()
        self._save(book)  # Update book

    def remove(self, pk):
        # смотрим нет ли заказов с этой книгой.
        order = session.query(Order).filter_by(book_id=pk).first()
        if order is not None:
            Helpers.print_color(f"Ошибка удаления. У книги есть активные заказы. {order.id}", "red")
            return False
        self._delete(pk=pk)


class OrderManager(BaseManager):
    def __init__(self):
        super().__init__()
        self.entity = Order

    def create(self, params: dict) -> int | bool:
        # существует ли пользователь
        try:
            user_id = int(params["user_id"])
            user = session.query(User).filter_by(id=user_id).first()
            if user is None:
                self.last_error = f"Пользователь '{user_id}' не найден"
                return False
        except ValueError:
            self.last_error = f"Данные по пользователь {params['user_id']} запросить не удалось"
            return False

        # количество
        try:
            quantity = int(params["quantity"])
            if quantity <= 0:
                self.last_error = "Введите количество > 0"
                return False
        except ValueError:
            self.last_error = "Введите корректное количество"
            return False

        # существует ли книга и достаточно ли в наличии
        try:
            book_id = int(params["book_id"])
            book = session.query(Book).filter_by(id=book_id).first()
            if book is None:
                self.last_error = f"Книга {book_id} не найдена"
                return False

            if quantity > book.amount:
                self.last_error = f"Не хватает книг. Доступно {book.amount} из {quantity}"
                return False
        except ValueError:
            self.last_error = f"Данные по книге '{params['book_id']}' запросить не удалось"
            return False

        # проверка достаточный ли баланс для покупки
        if user.balance <= 0 or user.balance < book.price * quantity:
            self.last_error = f"Недостаточно средств. Необходимо - {book.price * quantity}, доступно - {user.balance}"
            return False


        try:
            # сохраняем заказ
            order = Order(
                user_id=user.id,
                book_id=book.id,
                quantity=quantity
            )

            session.add(order)
            session.flush()

            if order.id is not None:
                # сохраняем новый баланс пользователя
                user.balance = user.balance - book.price * quantity
                session.add(user)
                session.flush()
                # уменьшаем количество книг
                book.amount = book.amount - quantity
                session.add(book)
                session.flush()

                session.commit()
                return order.id
        except IntegrityError as e:
            print(e)
            Helpers.print_color("Возврат назад...", "red")
            session.rollback()
            Helpers.print_color("Транзакция не удалась.", "red")

        return False

    def update(self, id: int, params: dict) -> None | bool:
        # TODO при случае сделать обновление
        pass

    def remove(self, pk):
        try:
            order = session.query(Order).filter_by(id=pk).first()

            book = session.query(Book).filter_by(id=order.book_id).first()
            user = session.query(User).filter_by(id=order.user_id).first()

            # добавляем пользователю в баланс стоимость книг
            user.balance += book.price * order.quantity
            session.add(user)
            session.flush()

            # обновляем количество книг
            book.amount += order.quantity
            session.add(book)
            session.flush()

            # удаляем заказ
            session.delete(order)
            session.commit()

        except IntegrityError as e:
            print(e)
            Helpers.print_color("Возврат назад...", "red")
            session.rollback()
            Helpers.print_color("Транзакция не удалась.", "red")


class GenreManager(BaseManager):
    def __init__(self):
        super().__init__()
        self.entity = Genre

    def add(self, params: dict) -> int | bool:

        name = Helpers.htmlspecialchars(params["name"])
        if len(name) < 3:
            self.last_error = "Введите название жанра"
            return False

        genre = self.entity(
            name=name
        )

        self._save(genre)  # Add genre

        if genre.id is not None:
            return genre.id
        return False

    def update(self, id: int, params: dict) -> None | bool:
        genre = self.get_by_id(pk=id)
        if genre is None:
            self.last_error = f"Жанр {id} не найдена"
            return False

        if len(params["name"]) >= 3:
            genre.name = Helpers.htmlspecialchars(params["name"])

        genre.updated_at = datetime.now()
        self._save(genre)  # Update book

    def remove(self, pk):
        # На все книги (в таблице book) с жанром который удаляем ставим None
        book = session.query(Book).filter_by(genre_id=pk).all()
        if len(book) > 0:
            for elem in book:
                elem.genre_id = None
                self._save(elem)
        self._delete(pk=pk)
