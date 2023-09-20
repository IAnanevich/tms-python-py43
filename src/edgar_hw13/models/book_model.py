from sqlalchemy import Column, String, Integer, Float, ForeignKey, Text
from sqlalchemy.orm import relationship

from src.edgar_hw13.models.base_model import BaseModel


class Book(BaseModel):
    """
    The BookModel class is a subclass of the BaseModel class and represents a model for books in the application.
    """
    __tablename__ = 'books'

    title = Column('title', String(20), nullable=False)
    description = Column('description', Text(100))
    amount = Column('amount', Integer, nullable=False, default=1)
    price = Column('price', Float, nullable=False, default=0)

    genre_id = Column('genre_id', Integer, ForeignKey('genres.id'))

    genre = relationship('Genre', foreign_keys=[genre_id])
