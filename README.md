# Library Management System

## Overview

This Library Management System allows users to perform basic operations such as adding books, borrowing books, returning books, and viewing available books. It is implemented in Python and follows Test-Driven Development (TDD) principles.

## Features

- **Add Books**: Add new books to the library with a unique identifier, title, author, and publication year.
- **Borrow Books**: Borrow a book if it is available.
- **Return Books**: Return a borrowed book and update its availability.
- **View Available Books**: View a list of all books currently available in the library.

## Requirements

- Python 3.x
- `pytest` (for running tests)
- `pytest-html` (for generating HTML reports)

## Installation and Setup

Follow these steps to set up the project on a Windows system:

1. **Clone the Repository**

    Open Command Prompt or PowerShell and run:

    ```
    git clone https://github.com/gp352/lib_management_system.git
    cd <repository-directory>
    ```

    Replace `<repository-directory>` with the directory name where the repository is cloned.

2. **Set Up a Virtual Environment**

    ```
    python -m venv venv
    ```

3. **Activate the Virtual Environment**

    ```
    venv\Scripts\activate
    ```

4. **Install Dependencies**

    Create a `requirements.txt` file if it doesn’t already exist and include the following:

    ```text
    pytest
    pytest-html
    ```

    Install the dependencies using:

    ```
    pip install -r requirements.txt
    ```

5. **Install Additional Testing Plugin** (for HTML reports)

    If not already included in `requirements.txt`, install `pytest-html` separately:

    ```
    pip install pytest-html
    ```

## Usage

1. **Run the Library Management System**

    You can import and use the `Library` class from the `library.py` file in a Python script or interactive session. Example usage:

    ```python
    from library import Library

    lib = Library()
    lib.add_book("1234567890", "Book Title", "Author Name", 2024)
    lib.borrow_book("1234567890")
    available_books = lib.view_available_books()
    ```

2. **Add, Borrow, Return, and View Books**

    - **Add Book**: `lib.add_book(isbn, title, author, year)`
    - **Borrow Book**: `lib.borrow_book(isbn)`
    - **Return Book**: `lib.returnbook(isbn)`
    - **View Available Books**: `lib.view_available_books()`

## Running Tests

1. **Run All Tests**

    To execute all test cases, use:

    ```
    pytest test_library.py
    ```

2. **Generate Test Report** (optional)

    To generate an HTML report of test results, use:

    ```
    pytest --html=report.html
    ```

    The report will be saved as `report.html` in the current directory.





