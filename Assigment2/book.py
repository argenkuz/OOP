class Book:
    def __init__(self, title=None, author=None, isbn=None, price=None, publisher=None, genre=None, page_count=None, publication_year=None):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.price = price
        self.publisher = publisher
        self.genre = genre
        self.page_count = page_count
        self.publication_year = publication_year

    def display_info(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"ISBN: {self.isbn}")
        print(f"Price: ${self.price}")
        print(f"Publisher: {self.publisher}")
        print(f"Genre: {self.genre}")
        print(f"Page Count: {self.page_count}")
        print(f"Publication Year: {self.publication_year}")

    def read_sample(self):
        print(f"Reading a sample of '{self.title}' by {self.author}...")

    def get_book_age(self):
        from datetime import datetime
        current_year = datetime.now().year
        age = current_year - self.publication_year if self.publication_year else "Unknown"
        print(f"The book '{self.title}' is {age} years old.")
