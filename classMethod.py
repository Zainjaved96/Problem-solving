class Book:
    Types = ("Hardcover", "Comic")

    def __init__(self, name, book_type, weight):
        self.name = name
        self.book_type = book_type
        self.weight = weight

    def __repr__(self):
        return f"<Book is {self.name} type is {self.book_type} and weight is {self.weight}"

    @classmethod
    def hardcover(cls, name, weight):
        return Book(name, Book.Types[0], weight + 20)

    @classmethod
    def comic(cls, name, weight):
        return Book(name, Book.Types[1], weight)


book1 = Book.hardcover("Song of ice and fire", 190)
book2 = Book.comic("Batman vs Superman Vol 1", 90)
print(book1)
print(book2)