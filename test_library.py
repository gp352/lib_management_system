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

