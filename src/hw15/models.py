from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class CatFact(Base):
    """
    Модель для хрaнения фактов о кошкaх.
    """

    __tablename__ = 'cat_facts'

    id: int = Column(Integer, primary_key=True)
    fact: str = Column(String)

    def __repr__(self) -> str:
        return f'CatFact(id={self.id}, fact={self.fact})'
