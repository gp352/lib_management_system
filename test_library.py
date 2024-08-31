import pytest
from library import Library

def test_add_book():
    library = Library()
    library.add_book("1234567890", "Book Title", "Author Name", 2024)
    book = library.get_book("1234567890")
    assert book is not None
    assert book['title'] == "Book Title"
    assert book['author'] == "Author Name"
    assert book['year'] == 2024

def test_add_book_duplicate_isbn():
    library = Library()
    library.add_book("1234567890", "First Book", "Author A", 2024)
    with pytest.raises(ValueError) as excinfo:
        library.add_book("1234567890", "Second Book", "Author B", 2024)
    assert str(excinfo.value) == "Book with this ISBN already exists"

def test_borrow_book_success():
    library = Library()
    library.add_book("987654321", "Book Name", "Author", 2022)
    library.borrow_book("987654321")
    book = library.get_book("987654321")
    assert book is not None
    assert book.get('borrowed') is True

def test_borrow_book_not_available():
    library = Library()
    library.add_book("987654321", "Book Name", "Author", 2022)
    library.borrow_book("987654321")
    with pytest.raises(ValueError) as excinfo:
        library.borrow_book("987654321")
    assert str(excinfo.value) == "Book borrowed already"

def test_borrow_nonexistent_book():
    library = Library()
    with pytest.raises(KeyError) as excinfo:
        library.borrow_book("nonexistent_isbn")
    assert excinfo.value.args[0] == "Book is not there"
    
def test_return_book_executed():
    library = Library()
    library.add_book("15643219656", "Book Name", "Author", 2022)
    library.borrow_book("15643219656")
    library.returnbook("15643219656")
    book = library.get_book("15643219656")
    assert book is not None
    assert book.get('borrowed') is False

def test_return_book_not_borrowed():
    library = Library()
    library.add_book("15643219656", "Book Name", "Author", 2022)
    with pytest.raises(ValueError) as excinfo:
        library.returnbook("15643219656")
    assert str(excinfo.value) == "Book is already in library"

def test_return_nonexistent_book():
    library = Library()
    with pytest.raises(KeyError) as excinfo:
        library.returnbook("nonexistent_isbn")
    assert excinfo.value.args[0] == "Book is not there"
def test_view_no_books_available():
    library = Library()
    available_books = library.view_available_books()
    assert len(available_books) == 0  # No books added yet

def test_view_all_books_available():
    library = Library()
    library.add_book("1111111111", "Harry Potter", "Author A", 2020)
    library.add_book("2222222222", "5 AM CLUB", "Author B", 2021)
    available_books = library.view_available_books()
    assert len(available_books) == 2
    assert available_books[0]['title'] == "Harry Potter"
    assert available_books[1]['title'] == "5 AM CLUB"

def test_view_some_books_borrowed():
    library = Library()
    library.add_book("1111111111", "Harry Potter", "Author A", 2020)
    library.add_book("2222222222", "5 AM CLUB", "Author B", 2021)
    library.add_book("3333333333", "Bhagvad Gita", "Author C", 2022)
    library.borrow_book("3333333333")
    available_books = library.view_available_books()
    assert len(available_books) == 2
    assert available_books[0]['title'] == "Harry Potter"
    assert available_books[1]['title'] == "5 AM CLUB"

    


