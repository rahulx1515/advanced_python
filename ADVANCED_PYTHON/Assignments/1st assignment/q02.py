class Book:
    def _init_(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn

    def display(self):
        return f"Title: {self.title}, Author: {self.author}, ISBN: {self.isbn}"

class Library:
    def _init_(self):
        self.books = []

    def add_book(self, title, author, isbn):
        self.books.append(Book(title, author, isbn))

    def view_books(self):
        if not self.books:
            return "No books in the library."
        return "\n".join(book.display() for book in self.books)

    def search_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                return book.display()
        return "Book not found."

# Menu-driven program
library = Library()
while True:
    print("\n1. Add Book\n2. View All Books\n3. Search Book\n4. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        title = input("Enter book title: ")
        author = input("Enter author: ")
        isbn = input("Enter ISBN: ")
        library.add_book(title, author, isbn)
    elif choice == 2:
        print("\nBooks in Library:")
        print(library.view_books())
    elif choice == 3:
        search_title = input("Enter title to search: ")
        print(library.search_book(search_title))
    elif choice == 4:
        break
    else:
        print("Invalid choice. Please try again.")