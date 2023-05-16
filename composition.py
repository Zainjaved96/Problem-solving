from typing import List


class Book:
    def __init__(self, name:str, pages:int) :
        self.name = name
        self.pages = pages

    def __str__(self) -> str:
        return f"{self.name} has {self.pages} pages"


class BookShelf:
    def __init__(self, books: List[Book]):
        self.books = books

    def __str__(self):
        return f"Book Shelf has {len(self.books)} books"


book1 = Book("Harry Potter", 256)
book2 = Book("The song of ice and fire", 4506)
bookshelf = BookShelf(book1, book2)
print(bookshelf)
