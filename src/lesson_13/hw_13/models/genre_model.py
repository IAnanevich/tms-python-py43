from sqlalchemy import Column, String

from src.lesson_13.hw_13.models.base_model import BaseModel


class Genre(BaseModel):
    """
    The GenreModel class is a subclass of the BaseModel class and represents a model for genres in the application.
    """
    __tablename__ = 'genres'

    name = Column('name', String(20), nullable=False)
