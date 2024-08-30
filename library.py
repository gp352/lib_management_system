# library.py
class Library:
    def __init__(self):
        self.books = {}

    def add_book(self, isbn, title, author, year):
        if isbn in self.books:
            raise ValueError("Book with this ISBN already exists")
        self.books[isbn] = {'title': title, 'author': author, 'year': year}

    def get_book(self, isbn):
        return self.books.get(isbn)
