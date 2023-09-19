import config
from manager import UserManager, BookManager, OrderManager, GenreManager
from helpers import Helpers
from models import User, Order, Book, Genre


# меню немного изменил. не по ТЗ. привычней выбрать сущность и потом что то с ней делать (добавить, удалить...)
def menu(user=UserManager(), book=BookManager(), order=OrderManager(), genre=GenreManager()):
    def sub_menu_1():  # заказы
        # показываем список первых LIMIT_ITEM_PAGE
        cur_page = 1
        items = order.list(limit=config.LIMIT_ITEM_PAGE, page=cur_page)
        for item in items:
            print(item.updated_at)
            for x in dir(item):
                print(x)
        if items:
            Helpers.print_list(items)
        else:
            Helpers.print_color("Список заказов пуст", "red")
        while (ch := input(config.MENU["sub_menu_1"])) != '0':
            if ch == '1':  # Изменить
                try:
                    id = int(input("Введите ID редактируемой записи: "))
                except ValueError:
                    Helpers.print_color("Введите корректный ID", "red")
                    break

                info = order.list(filter=(Order.id == id))
                if info:
                    Helpers.print_list(info)

                    params = {
                        "user_id": input("Пользователь (user_id): "),
                        "book_id": input("Книга (book_id): "),
                        "quantity": input("Кол-во книг: "),
                    }
                    order.update(id, params)
                    print("Заказ после обновления")

                    info = order.list(filter=(Order.id == id))
                    Helpers.print_list(info)
                else:
                    Helpers.print_color(f"Заказ с ID - {id} найти не удалось", "red")
            if ch == '2':  # Добавить
                print("Создание заказа")

                params = {
                    "user_id": input("* Пользователь (user_id): "),
                    "book_id": input("* Книга (book_id): "),
                    "quantity": input("* Кол-во книг: "),
                }
                id = order.create(params)
                if id != False and id > 0:
                    Helpers.print_color(f"ID добавленного заказа {id}", "green")
                    info = order.list(filter=(Order.id == id))
                    Helpers.print_list(info)
                else:
                    Helpers.print_color(f"Заказ не добавлен. {order.last_error}", "red")
            if ch == '3':  # Удалить
                Helpers.print_color("Удаляем заказ", "red")
                try:
                    id = int(input("Введите ID записи для удаления: "))
                except ValueError:
                    Helpers.print_color("Введите корректный ID", "red")
                    break
                order.remove(pk=id)
                items = order.list(limit=config.LIMIT_ITEM_PAGE, page=cur_page)
                Helpers.print_list(items)
            if ch == '<':  # Назад
                cur_page -= 1
                point_menu_prev(order, cur_page)
            if ch == '>':  # Далее
                cur_page += 1
                point_menu_next(order, cur_page)

    def sub_menu_2():  # пользователи
        # показываем список первых LIMIT_ITEM_PAGE
        cur_page = 1
        items = user.list(limit=config.LIMIT_ITEM_PAGE, page=cur_page)

        if items:
            Helpers.print_list(items)
        else:
            Helpers.print_color("Список пользователей пуст", "red")

        while (ch := input(config.MENU["sub_menu_2"])) != '0':
            if ch == '1':  # Изменить
                try:
                    id = int(input("Введите ID редактируемой записи: "))
                except ValueError:
                    Helpers.print_color("Введите корректный ID", "red")
                    break

                # info = user.list(filter=(user.entity.property_list["id"] == id))
                info = user.list(filter=(User.id == id))
                Helpers.print_list(info)

                params = {
                    "first_name": input("Имя: "),
                    "last_name": input("Фамилия: "),
                    "email": input("Email: "),
                    "age": input("Возраст: "),
                    "balance": input("Баланс: "),
                }
                user.update(id, params)
                print("Пользователь после обновления")
                # info = user.list(filter=(user.entity.property_list["id"] == id))
                info = user.list(filter=(User.id == id))
                Helpers.print_list(info)
            if ch == '2':  # Добавить
                print("Добавляем пользователя")

                params = {
                    "first_name": input("* Имя: "),
                    "last_name": input("* Фамилия: "),
                    "email": input("* Email: "),
                    "age": input("Возраст: "),
                    "balance": input("Баланс: "),
                }
                id = user.add(params)
                if id != False and id > 0:
                    Helpers.print_color(f"ID добавленной записи {id}", "green")
                    # info = user.list(filter=(user.entity.property_list["id"] == id))
                    info = user.list(filter=(User.id == id))
                    Helpers.print_list(info)
                else:
                    Helpers.print_color(f"Пользователь не добавлен. {user.last_error}", "red")
            if ch == '3':  # Удалить
                Helpers.print_color("Удаляем пользователя", "red")
                try:
                    id = int(input("Введите ID записи для удаления: "))
                except ValueError:
                    Helpers.print_color("Введите корректный ID", "red")
                    break
                user.remove(pk=id)
                items = user.list(limit=config.LIMIT_ITEM_PAGE, page=cur_page)
                Helpers.print_list(items)
            if ch == '<':  # Назад
                cur_page -= 1
                point_menu_prev(user, cur_page)
            if ch == '>':  # Далее
                cur_page += 1
                point_menu_next(user, cur_page)

    def sub_menu_3():  # книги
        # показываем список первых LIMIT_ITEM_PAGE
        cur_page = 1
        items = book.list()
        if items:
            Helpers.print_list(items)
        else:
            Helpers.print_color("Список книг пуст", "red")

        while (ch := input(config.MENU["sub_menu_3"])) != '0':
            if ch == '1':  # Изменить
                try:
                    id = int(input("Введите ID редактируемой записи: "))
                except ValueError:
                    Helpers.print_color("Введите корректный ID", "red")
                    break

                # info = book.list(filter=(book.entity.property_list["id"] == id))
                info = book.list(filter=(Book.id == id))
                if info:
                    Helpers.print_list(info)

                    params = {
                        "name": input("Название книги: "),
                        "description": input("Описание: "),
                        "amount": input("Количество: "),
                        "price": input("Цена: "),
                        "genre_id": input("Жанр (ID из таблицы genre): "),
                    }
                    book.update(id, params)
                    print("Книга после обновления")
                    # info = book.list(filter=(book.entity.property_list["id"] == id))
                    info = book.list(filter=(Book.id == id))
                    Helpers.print_list(info)
                else:
                    Helpers.print_color(f"Книгу с ID - {id} найти не удалось", "red")
            if ch == '2':  # Добавить
                print("Добавляем книгу")

                params = {
                    "name": input("* Название книги: "),
                    "description": input("Описание: "),
                    "amount": input("Количество: "),
                    "price": input("Цена: "),
                    "genre_id": input("Жанр (ID из таблицы genre): "),
                }
                id = book.add(params)
                if id != False and id > 0:
                    Helpers.print_color(f"ID добавленной записи {id}", "green")
                    # info = book.list(filter=(book.entity.property_list["id"] == id))
                    info = book.list(filter=(Book.id == id))
                    Helpers.print_list(info)
                else:
                    Helpers.print_color(f"Книга не добавлена. {book.last_error}", "red")
            if ch == '3':  # Удалить
                Helpers.print_color("Удаляем книгу", "red")
                try:
                    id = int(input("Введите ID записи для удаления: "))
                except ValueError:
                    Helpers.print_color("Введите корректный ID", "red")
                    break
                book.remove(pk=id)
                items = book.list(limit=config.LIMIT_ITEM_PAGE, page=cur_page)
                Helpers.print_list(items)
            if ch == '<':  # Назад
                cur_page -= 1
                point_menu_prev(book, cur_page)
            if ch == '>':  # Далее
                cur_page += 1
                point_menu_next(book, cur_page)

    def sub_menu_4():  # жанры
        # показываем список первых LIMIT_ITEM_PAGE
        cur_page = 1
        items = genre.list()
        if items:
            Helpers.print_list(items)
        else:
            Helpers.print_color("Список жанров пуст", "red")

        while (ch := input(config.MENU["sub_menu_4"])) != '0':
            if ch == '1':  # Изменить
                try:
                    id = int(input("Введите ID редактируемой записи: "))
                except ValueError:
                    Helpers.print_color("Введите корректный ID", "red")
                    break

                info = genre.list(filter=(Genre.id == id))
                if info:
                    Helpers.print_list(info)

                    params = {
                        "name": input("Название жанра: ")
                    }
                    genre.update(id, params)
                    print("Жанр после обновления")

                    info = genre.list(filter=(Genre.id == id))
                    Helpers.print_list(info)
                else:
                    Helpers.print_color(f"Жанр с ID - {id} найти не удалось", "red")
            if ch == '2':  # Добавить
                print("Добавляем жанр")

                params = {
                    "name": input("* Название жанра: "),
                }
                id = genre.add(params)
                if id != False and id > 0:
                    Helpers.print_color(f"ID добавленной записи {id}", "green")
                    info = genre.list(filter=(Genre.id == id))
                    Helpers.print_list(info)
                else:
                    Helpers.print_color(f"Жанр не добавлен. {genre.last_error}", "red")
            if ch == '3':  # Удалить
                Helpers.print_color("Удаляем жанр", "red")
                try:
                    id = int(input("Введите ID записи для удаления: "))
                except ValueError:
                    Helpers.print_color("Введите корректный ID", "red")
                    break
                genre.remove(pk=id)
                items = genre.list(limit=config.LIMIT_ITEM_PAGE, page=cur_page)
                Helpers.print_list(items)
            if ch == '<':  # Назад
                cur_page -= 1
                point_menu_prev(genre, cur_page)
            if ch == '>':  # Далее
                cur_page += 1
                point_menu_next(genre, cur_page)

    # вынес в функции пункты меню Назад и Вперед. чуть сократить код)
    def point_menu_prev(obj: object, page: int = 1) -> None:
        if page <= 0:
            page = 1
        print(f"Страница {page}")
        items = obj.list(limit=config.LIMIT_ITEM_PAGE, page=page)
        Helpers.print_list(items)

    def point_menu_next(obj: object, page: int = 1) -> None:
        print(f"Страница {page}")
        items = obj.list(limit=config.LIMIT_ITEM_PAGE, page=page)
        Helpers.print_list(items)

    while (ch := input(config.MENU["main"])) != "0":
        if ch == '1':
            sub_menu_1()
        elif ch == '2':
            sub_menu_2()
        elif ch == '3':
            sub_menu_3()
        elif ch == '4':
            sub_menu_4()


if __name__ == '__main__':
    menu()
