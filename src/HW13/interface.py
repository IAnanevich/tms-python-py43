from create_mixin import create_reader, create_book, create_genre, create_order
from delete_mixin import delete_genre, delete_order, delete_reader, delete_book
from update_mixin import update_reader, update_book, update_genre, update_order
from list_mixin import read_reader_table, read_book_table, read_genre_table, read_order_table

while True:
    print('1.Create')
    print('2.Read')
    print('3.Update')
    print('4.Delete')
    print('0.Exit')

    choice = input('Enter your choice: ')
    if choice.isdigit():
        choice = int(choice)

        if choice == 1:
            create_choice = input('Enter your crete action: ')
            print('1.Create reader')
            print('2.Create book')
            print('3.Create genre')
            print('4.Create order')
            if create_choice == 1:
                create_reader()
            elif create_choice == 2:
                create_book()
            elif create_choice == 3:
                create_genre()
            elif create_choice == 4:
                create_order()
        elif choice == 2:
            read_choice = input('Enter your read action: ')
            print('1.Read reader')
            print('2.Read book')
            print('3.Read genre')
            print('4.Read order')
            if read_choice == 1:
                read_reader_table()
            elif read_choice == 2:
                read_book_table()
            elif read_choice == 3:
                read_genre_table()
            elif read_choice == 4:
                read_order_table()
        elif choice == 3:
            update_choice = input('Enter your update action: ')
            print('1.Update reader')
            print('2.Update book')
            print('3.Update genre')
            print('4.Update order')
            if update_choice == 1:
                update_reader()
            elif update_choice == 2:
                update_book()
            elif update_choice == 3:
                update_genre()
            elif update_choice == 4:
                update_order()
        elif choice == 4:
            delete_choice = input('Enter your delete action: ')
            print('1.Delete reader')
            print('2.Delete book')
            print('3.Delete genre')
            print('4.Delete order')
            if delete_choice == 1:
                delete_reader()
            elif delete_choice == 2:
                delete_book()
            elif delete_choice == 3:
                delete_genre()
            elif delete_choice == 4:
                delete_order()
        elif choice == 0:
            print('you are out')
            break
