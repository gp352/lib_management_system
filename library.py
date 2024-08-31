# library.py
# library.py
class Library:
    def __init__(self):
        self.books = {}

    def add_book(self, isbn, title, author, year):
        if isbn in self.books:
            raise ValueError("Book with this ISBN already exists")
        self.books[isbn] = {'title': title, 'author': author, 'year': year, 'borrowed': False}

    def get_book(self, isbn):
        return self.books.get(isbn)

    def borrow_book(self, isbn):
        book = self.get_book(isbn)
        if book is None:
            raise KeyError("Book is not there")
        if book['borrowed']:
            raise ValueError("Book borrowed already")
        book['borrowed'] = True
    
    def returnbook(self, isbn):
        book = self.get_book(isbn)
        if book is None:
            raise KeyError("Book is not there")
        if not book['borrowed']:
            raise ValueError("Book is already in library")
        book['borrowed'] = False