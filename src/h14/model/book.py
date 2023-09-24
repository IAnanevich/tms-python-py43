from sqlalchemy import Column, String, Integer, Float, ForeignKey, Text
from sqlalchemy.orm import relationship
from src.h14.model.base import BaseModel


class Book(BaseModel):
    """
    The Book class is a subclass of the BaseModel class
    """
    __tablename__ = 'books'
    title = Column('title', String(20), nullable=False)
    description = Column('description', Text(100))
    amount = Column('amount', Integer, nullable=False, default=0)
    price = Column('price', Float, nullable=False, default=0)
    genre_id = Column('genre_id', Integer, ForeignKey('genres.id'))
    genre = relationship('Genre', foreign_keys=[genre_id])
