class Library(object):
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


class Roman(Book):
    def __init__(self, name, publish_date, nr_of_volumes):
        super().__init__(name, publish_date)
        self.nr_of_volumes = nr_of_volumes


class ScientificPaper(Book):
    def __init__(self, name, publish_date, published_paper):
        super().__init__(name, publish_date)
        self.published_paper = published_paper


class Manuals(Book):
    def __init__(self, name, publish_date, editors):
        super().__init__(name, publish_date)
        self.editors = editors


baltagul = Roman('Baltagul', 1900, 1)
death_to_earth = ScientificPaper('We are killing the earth', 2021, 'Science Magazine')
manal_lb_romana = Manuals('Manualul limbii romane, clasa a VI-a', 1999, 'Editura Teora')




biblia = Book('Biblia', 2021)
libraria_Eminescu = Library('Libraria Mihai Eminescu')
libraria_Eminescu.show_menu()
libraria_Eminescu.add_new_book(biblia)
libraria_Eminescu.list_all_books()

libraria_Eminescu.add_new_book(Book('Cartea1', 2020))

print("-----------------")
libraria_Eminescu.list_all_books()


class Author:
    def __init__(self, name):
        self.name = name


class MultipleAuthor(Author):
    def __init__(self, *name):
        super().__init__(name)

    def __str__(self):
        print(x for x in self.name)


autori = MultipleAuthor('Cosmin', 'Vlad')

print(autori.name)
print(dir(autori))
