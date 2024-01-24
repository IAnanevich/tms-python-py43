from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base
from menu import Menu


engine = create_engine('sqlite:///IPinfo.db', echo=True)
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()
Base.metadata.create_all(bind=engine)


class IPInfo(Base):
    __tablename__ = 'IPInfo'
    id = Column('id', Integer, primary_key=True, autoincrement=True)
    ip = Column(String(15), nullable=False)
    city = Column(String(20), nullable=False)
    region = Column(String(20), nullable=False)
    country = Column(String(20), nullable=False)
    loc = Column(String(20), nullable=False)
    org = Column(String(50), nullable=False)
    postal = Column(Integer)
    timezone = Column(String(20), nullable=False)
    readme = Column(String(60), nullable=False)

while True:
    Menu.menu_viz(menu=menu_1)
    menu_1 = Menu.menu_imp(session=session, menu_name=menu_1, choose_input=input(' '))
    if menu_1 == 'Выход':
        break
