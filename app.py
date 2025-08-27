'''
* Pustakalaya version(2.0.0)
* app.py
'''

import json
from lib import Book, Member, Library

# Main Application class to manage Library system with persistence (JSON file).
class Application:

    # Initialize application with empty Library and set default file name.
    def __init__(self):
        self.lib = Library()
        self.filename = 'lib.json'  
        self.data = None            

    # main function ---
    def active(self):
        # Load existing data from JSON file before starting
        self.load_data()

        print('-' * 32)
        print(" Welcome in Pustakalaya version(2.0.0) ")
        print('-' * 32)
        print("1. Add Book")
        print("2. Add Member")
        print("3. Borrow Book")
        print("4. Return Book")
        print("5. List Books")
        print("6. List Available Books")
        print("7. List Members")
        print("0. Exit")
        print('=' * 32)

        # Continuous loop until user exits
        while True:
            try:
                choice = int(input("\n /// ENTER CHOICE NUMBER /// : "))
                print()
            except ValueError:
                print("~ Invalid input, enter number only")
                continue

            if choice == 0:  # Exit
                print("~ Pustakalaya version(2.0.0) is [CLOSED]")
                break

            elif choice == 1:  # Add book
                id = int(input("Enter book id: "))
                title = input("Enter book title: ")
                subtitle = input("Enter book subtitle: ")
                author = input("Enter author: ")
                year = input("Enter year: ")

                book = Book(id, title, subtitle, author, year)
                self.lib.add_book(book)

            elif choice == 2:  # Add member
                id = int(input("Enter member id: "))
                name = input("Enter member name: ")

                member = Member(id, name)
                self.lib.add_member(member)

            elif choice == 3:  # Borrow book
                book_id = int(input("Enter book id to borrow: "))
                member_id = int(input("Enter member id: "))
                self.lib.borrow_book(book_id, member_id)

            elif choice == 4:  # Return book
                book_id = int(input("Enter book id to return: "))
                member_id = int(input("Enter member id: "))
                self.lib.return_book(book_id, member_id)

            elif choice == 5:  # Show all books
                self.lib.book_list()

            elif choice == 6:  # Show only available books
                self.lib.book_list(only_available=True)

            elif choice == 7:  # Show all members
                self.lib.member_list()

            else:
                print("~ Invalid choice")

            # Save library data to file after every change
            self.save_data()

    # Save all books and members into JSON file.
    def save_data(self):
        # Convert Library data into dictionary
        self.data = {
            "books": [
                {
                    "id": b.id,
                    "title": b.title,
                    "subtitle": b.subtitle,
                    "author": b.author,
                    "year": b.year,
                    "isAvailable": b.isAvailable
                } for b in self.lib.books
            ],
            "members": [
                {
                    "id": m.id,
                    "name": m.name,
                    "borrow_books": m.borrow_books
                } for m in self.lib.members
            ]
        }

        # Write dictionary into JSON file
        with open(self.filename, 'w') as file:
            json.dump(self.data, file, indent=4)

        print('~ Data is updated in JSON file')

    # Load books and members from JSON file if exists.
    def load_data(self):
        try:
            with open(self.filename, 'r') as file:
                self.data = json.load(file)

            # Restore books
            for b in self.data.get("books", []):
                self.lib.add_book(Book(
                    b["id"],
                    b["title"],
                    b.get("subtitle"),
                    b.get("author"),
                    b.get("year"),
                    b.get("isAvailable", True)
                ))

            # Restore members
            for m in self.data.get("members", []):
                member = Member(m["id"], m["name"])
                member.borrow_books = m.get("borrow_books", [])
                self.lib.add_member(member)

        except FileNotFoundError:
            print("\n~ Welcome! New library file will be created.\n")


if __name__ == "__main__":

    # Create Application and start menu
    app = Application()
    
    app.active()

# developed by Alisha | (https://alishabeg.github.io/AlishaBeg) ---