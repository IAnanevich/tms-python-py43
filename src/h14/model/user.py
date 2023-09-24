from sqlalchemy import Column, String, Integer, Float
from src.h14.model.base import BaseModel


class Human(BaseModel):
    """
    The Book class is a subclass of the BaseModel class
    """
    __tablename__ = 'humans'
    first_name = Column('first_name', String(20), nullable=False)
    last_name = Column('last_name', String(30), nullable=False)
    email = Column('email', String(50), unique=True, nullable=False)
    age = Column('age', Integer, nullable=False)
    balance = Column('balance', Float, nullable=False, default=0)
