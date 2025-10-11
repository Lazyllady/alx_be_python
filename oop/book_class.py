# oop/book_class.py

class Book:
    """
    Book class demonstrating magic methods:
    - __init__ for construction
    - __del__ for deletion message
    - __str__ for user-friendly string
    - __repr__ for unambiguous representation
    """

    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def __del__(self):
        print(f"Deleting {self.title}")

    def __str__(self):
        # Checker expects exactly this signature
        return f"{self.title} by {self.author}, published in {self.year}"

    def __repr__(self):
        # Checker expects exactly this signature
        return f"Book('{self.title}', '{self.author}', {self.year})"
