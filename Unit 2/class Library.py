# develop a library class that has instance variable like book_name, author, and availability status.
# the class should provide methods to check out a book, return a book, and display available books.
# use the __init__ constructor to initialize book details for each object
class Library:
    def __init__(self, book_name, author, available=True):
        self.book_name = book_name
        self.author = author
        self.available = available
        
    def check_out(self):
        if self.available:
            self.available = False
            print(f"the book {self.book_name} has been checked out")
        else:
            print(f"the book {self.book_name} is not available")    

    def return_book(self):
        self.available = True
        print(f"the book {self.book_name} has been returned and is now available")

    def display_book(self):
        self.available = True
        print(f"the book {self.book_name} by {self.author} is available")

book1 = Library("Mein Kampf", "Adolf Hitler")

book1.check_out()
book1.display_book()
book1.return_book()

book2 = Library("Wings of Fire", "Dr.Abdul Kalam")

book2.check_out()
book2.return_book()
book2.display_book()
