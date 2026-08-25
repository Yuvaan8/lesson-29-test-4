from abc import ABC, abstractmethod
class LibraryItem(ABC):
    def __init__(self, title, item_id):
        self.title = title
        self.item_id = item_id
        self.is_borrowed = False
    abstractmethod
    def get_item(self):
        pass
    def borrow(self):
        if not self.is_borrowed:
            print(f'you have borrowed {self.title}')
            self.is_borrowed = True
        else:
            print(f'you have already borrowed {self.title}')
    def return_item(self):
        if self.is_borrowed:
            print(f'you have returned {self.title}')
            self.is_borrowed = False
        else:
            print(f'you have not borrowed {self.title}')
    def get_item(self):
        return self
class Book(LibraryItem):
    def __init__(self, title, item_id, author):
        super().__init__(title, item_id)
        self.author = author
        print(f'you borrowed {self.title} by {self.author}')
my_book = Book('The Hobbit', 'C021', 'J.R.R Tolkein')
my_book.borrow()
my_book.borrow()
my_book.return_item()
        
    