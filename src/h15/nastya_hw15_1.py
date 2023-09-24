import requests
from sqlalchemy import create_engine, Column, Integer, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

url = 'https://catfact.ninja/fact'
print(requests.get(url).json())

engine = create_engine('sqlite:///nya.db', echo=True)
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()


class Cats(Base):
    """
    The Cats class is a subclass of Base from SQLAlchemy's
    """
    fact = Column('fact', Text(100), primary_key=True, nullable=False)
    length = Column('length', Integer)


while True:
    try:
        print("[1]Create")
        print("[2]Read")
        print("[0]Exit")
        choice = int(input("Enter your choice: "))
        if choice == 0:
            break
        elif choice == 1:
            try:
                fact = input('Enter fact: ')
                length = int(input('Enter length: '))
                cat = Cats(fact=fact, length=length)
                session.add(cat)
                session.commit()
            except Exception as e:
                print(e)
        elif choice == 2:
            try:
                cats = session.query(Cats).scalars().all()
                for cat in cats:
                    print(cat.fact, cat.length)
            except Exception as e:
                print(e)
    except Exception as e:
        print(e)
