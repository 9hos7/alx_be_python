class Book:
    def __init__(self, author, title):
        self.author = author
        self.title = title
        self.is_checked_out = False
        
    def check_out(self):
        if not self.is_checked_out:
            self.is_checked_out = True
            return True
        return False
    
    def return_book(self):
        if self.is_checked_out:
            self.is_checked_out = False
            return False
        return True

class Library():

    def __init__(self):
        self._books = []
    
    def add_book(self, book):
        self._books.append(book)

    def check_out_book(self, title):
        for book in self._books:
            if book.title.lower() == title.lower():
                if book.check_out():
                    print(f"You have checked out '{book.title}'.")
                else:
                    print(f"'{book.title}' is already checked out.")
                return
        print(f"No book with the title '{title}'.")
    
    def return_book(self, title):
        for book in self._books:
            if book.title.lower() == title.lower():
                if book.return_book():
                    print(f"You have returned '{title}'.")
                else:
                    print(f"'{title}' was not checked out.")
                return
            print(f"No book with the title '{title}'.")

    def list_available_books(self):
        available_books = [book for book in self._books if not book.is_checked_out]
        if available_books:
            print("Available Books: ")
            for book in available_books:
                print(f"- {book.title}")
        else:
            print("No books are currently available.")
        