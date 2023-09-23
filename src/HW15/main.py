from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker
from Homework_15.menu import Menu
from mixins import AdressMixin
from sqlalchemy import create_engine


engine = create_engine('sqlite:///ip_location.db', echo=True)
Session = sessionmaker(bind=engine)
Base = declarative_base()
session = Session()

while True:
    choice = Menu.main_menu()
    if choice == '1':
        any_choice = Menu.create_menu()
        if any_choice == '1':
            AdressMixin.get_ip(session=session)

    elif choice == '2':
        _choice = Menu.list_menu()
        if _choice == '1':
            AdressMixin.read_table(session=session)

    elif choice == '0':
        print('Bye')
        break

    Base.metadata.create_all(bind=engine)

