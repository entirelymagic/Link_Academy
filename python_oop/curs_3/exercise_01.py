class Library:
    """Class that contain a list of book objects and perform actions on them"""

    def __init__(self, name):
        self.name = name
        self.book_list = []

    MAIN_MENU = """
    1. Add new book.
    2. Modify the details of the book.
    3. Delete the book.
    4. List all books
    5. Exit
    """

    MENU_OPTIONS = {
        1: "Add books",
        2: "Modify books",
        3: "delete book",
        4: "list_all books",
        5: "Exit"
    }

    @classmethod
    def show_menu(cls):
        print(cls.MAIN_MENU)

    def add_new_book(self, book):
        self.book_list.append(book)

    def list_all_books(self):
        print('This are the books available in our library:')
        for book in self.book_list:
            print(f'{self.book_list.index(book)+1}.{book.name} published in {book.publish_Date}')

    def delete_book(self, book):
        self.book_list.remove(book)


class Book:
    def __init__(self, name, publish_date):
        self.name = name
        self.publish_Date = publish_date

    def __str__(self):
        return self.name


biblia = Book('Biblia', 2021)
libraria_Eminescu = Library('Libraria Mihai Eminescu')
libraria_Eminescu.show_menu()
libraria_Eminescu.add_new_book(biblia)
libraria_Eminescu.list_all_books()

libraria_Eminescu.add_new_book(Book('Cartea1', 2020))

print("-----------------")
libraria_Eminescu.list_all_books()

