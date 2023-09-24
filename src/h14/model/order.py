from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from src.h14.model.base import BaseModel


class Order(BaseModel):
    """
    The BookModel class is a subclass of the BaseModel class
    """
    __tablename__ = 'orders'
    book_id = Column('user_id', Integer, ForeignKey('users.id'))
    user_id = Column('book_id', Integer, ForeignKey('books.id'))
    human = relationship("Human", foreign_keys=[user_id])
    book = relationship("Book", foreign_keys=[book_id])
