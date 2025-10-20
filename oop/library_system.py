class Book:
    def __init__(self, title, author, **kwargs):
        super().__init__(**kwargs)
        self.title = str(title)
        self.author = str(author)

class EBook(Book):
    def __init__(self, title, author, file_size, **kwargs):
        super().__init__(title=title, author=author, **kwargs)
        self.file_size = int(file_size)

class PrintBook(Book):
    def __init__(self, title, author, page_count, **kwargs):
        super().__init__(title=title, author=author, *kwargs)
        self.page_count = int(page_count)

class Library:
    def __init__(self):
        self._book = []

    def add_book(self, book):
        self._book.append(book)

    def list_books(self):
        if not self._book:
            print("No book available at this time.")
        else:
            print("Available books in the library: ")
            for book in self._book:
                if isinstance(book, EBook):
                    print(f"EBook - Title: {book.title}, Author: {book.author}, File Size: {book.file_size}MB")
                elif isinstance(book, PrintBook):
                    print(f"Print Book - Title: {book.title}, Author: {book.author}, Page Count: {book.page_count} pages")
                else:
                    print(f"Book - Title: {book.title}, Author: {book.author}")