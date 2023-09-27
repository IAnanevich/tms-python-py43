import requests
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, CatFact

engine = create_engine('sqlite:///cat_facts.db')
Base.metadata.create_all(bind=engine)
Session = sessionmaker(bind=engine)
session = Session()


def create_cat_fact() -> None:
    """
    Создаeт зaпись о случайном фaкте о кошках и сохраняет его в базе данных.
    """
    response = requests.get('https://catfact.ninja/fact')
    data = response.json()
    fact = CatFact(fact=data['fact'])
    session.add(fact)
    session.commit()
    print('Запись успешно создана!')


def read_cat_facts() -> None:
    """
    Выводит все записи о фактах о кошках из базы данных.
    """
    cat_facts = session.query(CatFact).all()
    for cat_fact in cat_facts:
        print(cat_fact)


def main() -> None:
    """
    Главная функция программы. Выводит меню и обрабатывает выбор пользователя.
    """
    while True:
        print('Меню:')
        print('1. Создать запись')
        print('2. Прочитать все записи')
        print('0. Выйти')

        choice = input('Выберите действие: ')

        if choice == '1':
            create_cat_fact()
        elif choice == '2':
            read_cat_facts()
        elif choice == '0':
            break
        else:
            print('Неверный выбор. Попробуйте снова.')


if __name__ == '__main__':
    main()
