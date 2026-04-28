"""Library Management System (Constructor & Inheritance) 
A library stores information about books and digital books. Create a base class Book 
with a constructor to initialize book details. Create a derived class EBook that adds file 
size information. ."""

class Book:
    def __init__(self, title, price):
        self.title = title
        self.price = price

    def book_details(self):
        print("Title:", self.title)
        print("Price:", self.price)

class EBook(Book):
    def __init__(self, title, price, file_size):
        super().__init__(title, price)
        self.file_size = file_size

    def book_details(self):
        super().book_details()
        print("File Size:", self.file_size, "MB")

book = Book("The Pride and Prejudice", 500)
ebook = EBook("Atomic Habits", 350, 5)

print("Book:")
book.book_details()

print("\nE-Book:")
ebook.book_details()
        
