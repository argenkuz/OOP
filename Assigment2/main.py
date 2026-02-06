import os
from book import Book

n = int(input("How many books do you want to create? "))
books = []

for i in range(n):
    title = input("Enter the title of the book: ")
    author = input("Enter the author of the book: ")
    isbn = input("Enter the ISBN of the book: ")
    price = float(input("Enter the price of the book: "))
    publisher = input("Enter the publisher of the book: ")
    genre = input("Enter the genre of the book: ")
    page_count = int(input("Enter the number of pages in the book: "))
    publication_year = int(input("Enter the publication year of the book: "))


    book = Book(title, author, isbn, price, publisher, genre, page_count, publication_year)
    books.append(book)

for book in books:
    print("-----" * 5)
    book.display_info()
    book.read_sample()
    book.get_book_age()
    print("-----" * 5)
