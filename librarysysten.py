class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False
    def borrow(self):
        if self.is_borrowed:
            print(f"Sorry, '{self.title}' is already borrowed.")
        else:
            self.is_borrowed = True
            print(f"You have successfully borrowed '{self.title}'.")
    def return_book(self):
        if not self.is_borrowed:
            print(f"'{self.title}' was not borrowed, so it cannot be returned.")
        else:
            self.is_borrowed = False
            print(f"Thank you for returning '{self.title}'.")
    def __str__(self):
        status = "Borrowed" if self.is_borrowed else "Available"
        return f"'{self.title}' by {self.author} [{status}]"
book1 = Book("Percy Jackson and the Olympians", "Rick Riordan")
book2 = Book("The Hobbit", "J.R.R. Tolkien")
book3 = Book("To Kill a Mockingbird", "Harper Lee")
print("=" * 42)
print("          LIBRARY SYSTEM")
print("=" * 42)
print("\nInitial Book Status ")
print(book1)
print(book2)
print(book3)
print("\n Borrowing Books")
book1.borrow()
book2.borrow()
print("\n Testing Double Borrowing Guard")
book1.borrow()
print("\n Returning Books")
book1.return_book()
print("\n Testing Return Not Borrowed Guard")
book3.return_book()
print("\n--- Updated Book Status ---")
print(book1)
print(book2)
print(book3)
