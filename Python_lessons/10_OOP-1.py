class Book:

    is_borrowed = False

    def __init__(self, title, author):
        self.title = title
        self.autor = author

    def borrow_book(self):
        self.is_borrowed = True

    def return_book(self):
        self.is_borrowed = False

    def get_status(self):
        print("Взята") if self.is_borrowed else print("Доступна")


first_book = Book("Title1", "Autor1")
second_book = Book("Title2", "Autor2")

first_book.borrow_book()
second_book.borrow_book()
second_book.return_book()

first_book.get_status()
second_book.get_status()
