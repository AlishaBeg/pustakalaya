'''
* Pustakalaya version(2.0.0)
* lib.py
'''

# ---------------------------------
# book class contain infromation
# ---------------------------------
class Book:
    
    # constructor: create a book with id, title, subtitle, author, year and availability status
    def __init__(self, id=None, title=None, subtitle=None, author=None, year=None, isAvailable=True):

        if id is None or title is None:
            print("~ id and title is required for book")
            return

        self.id = id
        self.title = title
        self.subtitle = subtitle
        self.author = author
        self.year = year
        self.isAvailable = isAvailable

    # return string description of the book
    def toString(self):
        return f"{self.id} > {self.title} {self.subtitle} in year {self.year} by {self.author} is {'Available' if self.isAvailable else 'not available'}"

    # mark the book as borrowed
    def borrow(self):

        if not self.isAvailable:
            print("~ book is not available")
            return

        self.isAvailable = False
        print("~ book is borrow")

    # mark the book as returned
    def returned(self):

        if self.isAvailable:
            print("~ book is available")
            return

        self.isAvailable = True
        print("~ book is returnd")

# -----------------------------------------
# member contain id name or borrow books
# -----------------------------------------
class Member:
    
    # constructor: create a member with id, name, and empty borrow list
    def __init__(self, id=None, name=None, borrow_books=[]):

        if id is None or name is None:
            print("~ id and name is required in member")
            return

        self.id = id
        self.name = name
        self.borrow_books = []  # list contain id of book

    # return string description of the member
    def toString(self):
        return f"id {self.id} member name is {self.name} borrow {self.borrow_books}"

    # borrow a book (if available)
    def borrow(self, book=None):
        
        if book is None:
            print("~ borrow book is None")
            return
        
        if not book.isAvailable:
            print("~ book is not avialable")
            return

        book.isAvailable = False
        self.borrow_books.append(book.id)
        print(f"~ {self.name} borrowed {book.title}")

    # return a borrowed book
    def returned(self, book=None):
        
        if book is None:
            print("~ borrow book is None")
            return
        
        if book.isAvailable:
            print("~ book is already available")
            return

        if book.id not in self.borrow_books:
            print(f"~ {self.name} has not borrowed this book")
            return
        
        book.isAvailable = True
        self.borrow_books.remove(book.id)
        print(f"~ {self.name} returned {book.title}")

# -----------------------------------
# library control books and members
# -----------------------------------
class Library:
    
    # constructor: keeps track of books and members
    def __init__(self):
        self.books = []
        self.members = []

    # check if member exists by id
    def memberExist(self, member_id):

        if member_id is None:
            print("~ member id is required")
            return

        for member in self.members:
            if member.id == member_id:
                return member
        
        return None

    # check if book exists by id
    def bookExist(self, book_id):
        
        if book_id is None:
            print("~ book id is required")
            return

        for book in self.books:
            if book.id == book_id:
                return book
        return None

    # add a book to library
    def add_book(self, book):
        self.books.append(book)
        print(f"~ book {book.title} added")

    # add a member to library
    def add_member(self, member):
        self.members.append(member)
        print(f"~ member {member.name} added")

    # find a book by title
    def find_book(self, title):

        for book in self.books:
            if book.title.lower() == title.lower():
                return book
        
        return None

    # member borrows a book by ids
    def borrow_book(self, book_id=None, member_id=None):
        member = self.memberExist(member_id)
        book = self.bookExist(book_id)

        if book is None or member is None:
            print("~ book and member is not exist")
            return

        member.borrow(book)

    # member returns a book by ids
    def return_book(self, book_id=None, member_id=None):
        member = self.memberExist(member_id)
        book = self.bookExist(book_id)

        if book is None or member is None:
            print("~ book and member is not exist")
            return

        member.returned(book)

    # print list of members
    def member_list(self):

        if len(self.members) == 0:
            print('~ not any member')
            return

        for member in self.members:
            print(member.toString())

    # print list of books
    def book_list(self, only_available=False):

        if len(self.books) == 0:
            print('~ empty books')
            return

        if only_available:
            for book in self.books:
                if book.isAvailable:
                    print(book.toString())
            return

        for book in self.books:
            print(book.toString())    

# developed by Alisha | (https://alishabeg.github.io/AlishaBeg) ---