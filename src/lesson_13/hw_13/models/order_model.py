from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship

from src.lesson_13.hw_13.models.base_model import BaseModel


class Order(BaseModel):
    """
    The BookModel class is a subclass of the BaseModel class and represents a model for books in the application.
    """
    __tablename__ = 'orders.csv'

    user_id = Column('user_id', Integer, ForeignKey('users.id'))
    book_id = Column('book_id', Integer, ForeignKey('books.id'))

    human = relationship("User", foreign_keys=[user_id])
    book = relationship("Book", foreign_keys=[book_id])

