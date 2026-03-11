'''You are provided with a poorly structured Library Management script that:
•	Contains repeated conditional logic
•	Does not use reusable functions
•	Lacks documentation
•	Uses print-based procedural execution
•	Does not follow modular programming principles
Your task is to refactor the code into a proper format 
1.	Create a module library.py with functions:
o	add_book(title, author, isbn)
o	remove_book(isbn)
o	search_book(isbn)
2.	Insert triple quotes under each function and let Copilot complete the docstrings.
3.	Generate documentation in the terminal.
4.	Export the documentation in HTML format.
5.	Open the file in a browser.
'''

# Library Management System (Unstructured Version)
# This code needs refactoring into a proper module with documentation.
library_db = {}
# Adding first book
title = "Python Basics"
author = "John Doe"
isbn = "101"

if isbn not in library_db:
    library_db[isbn] = {"title": title, "author": author}
    print("Book added successfully.")
else:
    print("Book already exists.")

# Adding second book (duplicate logic)
title = "AI Fundamentals"
author = "Jane Smith"
isbn = "102"

if isbn not in library_db:
    library_db[isbn] = {"title": title, "author": author}
    print("Book added successfully.")
else:
    print("Book already exists.")

# Searching book (repeated logic structure)
isbn = "101"
if isbn in library_db:
    print("Book Found:", library_db[isbn])
else:
    print("Book not found.")

# Removing book (again repeated pattern)
isbn = "101"
if isbn in library_db:
    del library_db[isbn]
    print("Book removed successfully.")
else:
    print("Book not found.")

# Searching again
isbn = "101"
if isbn in library_db:
    print("Book Found:", library_db[isbn])
else:
    print("Book not found.")

# Refactored Code:
# library.py
library_db = {}
def add_book(title, author, isbn):
    """Add a book to the library database."""
    if isbn not in library_db:
        library_db[isbn] = {"title": title, "author": author}
        print("Book added successfully.")
    else:
        print("Book already exists.")
def remove_book(isbn):
    """Remove a book from the library database."""
    if isbn in library_db:
        del library_db[isbn]
        print("Book removed successfully.")
    else:
        print("Book not found.")
def search_book(isbn):
    """Search for a book in the library database."""
    if isbn in library_db:
        print("Book Found:", library_db[isbn])
    else:
        print("Book not found.")
if __name__ == "__main__":
    add_book("Python Basics", "John Doe", "101")
    add_book("AI Fundamentals", "Jane Smith", "102")
    search_book("101")
    remove_book("101")
    search_book("101")
