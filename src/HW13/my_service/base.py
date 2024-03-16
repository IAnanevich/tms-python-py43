from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base


def __create_engine():
    return create_engine('sqlite:///maxim_hw13.db', echo=True)


def __create_session(engine):
    session = sessionmaker(bind=engine)
    return session()


ENGINE = __create_engine()
SESSION = __create_session(ENGINE)

Base = declarative_base()
