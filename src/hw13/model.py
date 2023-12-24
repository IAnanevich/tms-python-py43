from sqlalchemy.orm import declarative_base, sessionmaker, relationship
from sqlalchemy import Column, Integer, String, DateTime, create_engine, Text, Float, ForeignKey
from datetime import datetime

Base = declarative_base()


class Genres(Base):
    __tablename__ = "Genres"
    id = Column('id', Integer, primary_key=True, autoincrement=True)
    name = Column(String(20), nullable=False)
    created_at = Column(DateTime(), default=datetime.now)
    updated_at = Column(DateTime(), default=datetime.now, onupdate=datetime.now)


class Books(Base):
    __tablename__ = "Books"
    id = Column('id', Integer, primary_key=True, autoincrement=True)
    genre_id = Column(Integer, ForeignKey('Genres.id'))
    title = Column(String(20), nullable=False)
    description = Column(Text(100))
    amount = Column(Integer, nullable=False, default=1)
    price = Column(Float, nullable=False, default=0)
    created_at = Column(DateTime(), default=datetime.now)
    updated_at = Column(DateTime(), default=datetime.now, onupdate=datetime.now)
    genre = relationship("Genres", foreign_keys=[genre_id])


class Humans(Base):
    __tablename__ = "Humans"
    id = Column('id', Integer, primary_key=True, autoincrement=True)
    first_name = Column(String(20), nullable=False)
    last_name = Column(String(30))
    email = Column(String(50))
    age = Column(Integer, nullable=False)
    balance = Column(Float, nullable=False, default=0)
    created_at = Column(DateTime(), default=datetime.now)
    updated_at = Column(DateTime(), default=datetime.now, onupdate=datetime.now)


class Orders(Base):
    __tablename__ = "Orders"
    id = Column('id', Integer, primary_key=True, autoincrement=True)
    human_id = Column(Integer, ForeignKey('Humans.id'))
    book_id = Column(Integer, ForeignKey('Books.id'))
    created_at = Column(DateTime(), default=datetime.now)
    updated_at = Column(DateTime(), default=datetime.now, onupdate=datetime.now)
    human = relationship("Humans", foreign_keys=[human_id])
    book = relationship("Books", foreign_keys=[book_id])


engine = create_engine("sqlite:///hw13.db", echo=True)
Sessions = sessionmaker(bind=engine)
session = Sessions()
Base.metadata.create_all(bind=engine)
