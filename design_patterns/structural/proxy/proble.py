# Designing ebook mobile app
class Ebook:
    def __init__(self, name) -> None:
        self.name = name
        self.load()

    def load(self):
        print(f"load {self.name} book")

    def show(self):
        print(f"show {self.name} book")


class Libarary:
    def __init__(self) -> None:
        self.books = []

    def add_book(self, book: Ebook):
        self.books.append(book)


if __name__ == "__main__":
    library = Libarary()
    book1 = Ebook("book1")
    book2 = Ebook("book2")
    book3 = Ebook("book3")
    library.add_book(book1)
    library.add_book(book2)
    library.add_book(book3)

    book1.show()
    # when we want to open library
    # we load all books in the memory. but we don't need them.
    # we need to load a book in memory when cients want to read it.
    # so we need a lazy-identify system.
