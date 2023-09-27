from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class CatFact(Base):
    __tablename__ = 'cat_facts'

    id = Column(Integer, primary_key=True)
    fact = Column(String)

    def __repr__(self):
        return f'CatFact(id={self.id}, fact={self.fact})'
