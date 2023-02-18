# Designing ebook mobile app
from abc import ABC, abstractmethod


class Book(ABC):
    # called 'service interface' in books
    name = ""

    def show(self):
        print(f"show {self.name} book")


class RealEbook(Book):
    # called 'service' in books
    def __init__(self, name) -> None:
        self.name = name
        self.load()

    def load(self):
        print(f"load {self.name} book")

    def show(self):
        print(f"show {self.name} book")


class ProxyEbook(Book):
    # called 'proxy' in books
    def __init__(self, name) -> None:
        self.name = name
        self.book = None

    def show(self):
        if self.book is None:
            self.book = RealEbook(self.name)
        self.book.show()


class Libarary:
    def __init__(self) -> None:
        self.books = []

    def add_book(self, book: Book):
        self.books.append(book)


if __name__ == "__main__":
    library = Libarary()
    book1 = ProxyEbook("book1")
    book2 = ProxyEbook("book2")
    book3 = ProxyEbook("book3")
    library.add_book(book1)
    library.add_book(book2)
    library.add_book(book3)

    book1.show()
