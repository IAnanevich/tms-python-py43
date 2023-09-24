from sqlalchemy import Column, String
from src.h14.model.base import BaseModel


class Genre(BaseModel):
    """
    The Genre class is a subclass of the BaseModel class
    """
    __tablename__ = 'genres'
    name = Column('name', String(20), nullable=False)
