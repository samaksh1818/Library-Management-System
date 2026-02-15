class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print("Book added successfully")

    def show_books(self):
        for book in self.books:
            book.display()

    def borrow_book(self, title):
        for book in self.books:
            if book.title == title:
                if book.available:
                    book.available = False
                    print("Book borrowed successfully")
                else:
                    print("Book is already borrowed")
                return
        print("Book not found")

    def return_books(self, title):
        for book in self.books:
            if book.title == title:
                if not book.available:
                    book.available = True
                    print("Book returned successfully")
                else:
                    print("Book was not borrowed")
                return
        print("Book not found")


class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.available = True

    def display(self):
        status = "Available" if self.available else "Borrowed"
        print(f"{self.title} by {self.author} ({status})")


#Objects

lib = Library()

b1 = Book("Python", "Samaksh")
b2 = Book("C++", "Abhi")

lib.add_book(b1)
lib.add_book(b2)

print("\n-- All Books --")
lib.show_books()

print("\n-- Borrow Python --")
lib.borrow_book("Python")

print("\n-- After Borrowing --")
lib.show_books()

print("\n-- Retrun Python --")
lib.return_books("Python")