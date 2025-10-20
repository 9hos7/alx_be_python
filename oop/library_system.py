class Book:
    def __init__(self, title, author, **kwargs):
        super().__init__(**kwargs)
        self.title = str(title)
        self.author = str(author)

    def __str__(self):
        return f"Book: {self.title} by {self.author}"

class EBook(Book):
    def __init__(self, title, author, file_size, **kwargs):
        super().__init__(title=title, author=author, **kwargs)
        self.file_size = int(file_size)

    def __str__(self):
        return f"EBook: {self.title} by {self.author}, File Size: {self.file_size}kB"

class PrintBook(Book):
    def __init__(self, title, author, page_count, **kwargs):
        super().__init__(title=title, author=author, *kwargs)
        self.page_count = int(page_count)

    def __str__(self):
        return f"Print Book: {self.title} by {self.author}, Page Count: {self.page_count}"

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def list_books(self):
        if not self.books:
            print("No book available at this time.")
        else:
            for book in self.books:
                print(book)