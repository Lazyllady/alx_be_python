# oop/book_class.py

class Book:
    """
    Simple Book class demonstrating Python magic methods:
    - __init__ for construction
    - __del__ for (optional) cleanup notification
    - __str__ for user-friendly string
    - __repr__ for an unambiguous reproducible representation
    """

    def __init__(self, title: str, author: str, year: int):
        self.title = str(title)
        self.author = str(author)
        self.year = int(year)

    def __del__(self):
        # Note: __del__ may not always be called on program exit, but in normal
        # reference-counting scenarios del object triggers this.
        print(f"Deleting {self.title}")

    def __str__(self) -> str:
        return f"{self.title} by {self.author}, published in {self.year}"

    def __repr__(self) -> str:
        # Using !r ensures strings are quoted and escaped properly
        return f"Book({self.title!r}, {self.author!r}, {self.year})"
