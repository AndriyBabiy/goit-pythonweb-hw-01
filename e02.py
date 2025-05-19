from abc import ABC, abstractmethod

class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

class LibraryInterface(ABC):
    @abstractmethod
    def add_book(self, book: Book):
        pass


    @abstractmethod
    def remove_book(self, book: Book):
        pass

    @abstractmethod
    def show_books(self):
        pass

class Library(LibraryInterface):
    def __init__(self):
        self.books = []

    def add_book(self, book: Book):
        self.books.append(book)

    def remove_book(self, book: Book):
        self.books.remove(book)

    def show_books(self):
        for book in self.books:
            print(f'Title: {book.title}, Author: {book.author}, Year: {book.year}')

class LibraryManager:
    def __init__(self, library: Library):
        self.library = library

    def add_book(self, title, author, year):
        book = Book(title, author, year)
        return self.library.add_book(book)

    def remove_book(self, title):
        for book in self.library.books:
            if book.title == title:
                self.library.remove_book(book)
                break

    def show_books(self):
        self.library.show_books()

def main():
    library = Library()
    manager = LibraryManager(library)

    while True:
        command = input("Enter command (add, remove, show, exit): ").strip().lower()

        if command == "add":
            title = input("Enter book title: ").strip()
            author = input("Enter book author: ").strip()
            year = input("Enter book year: ").strip()
            manager.add_book(title, author, year)
        elif command == "remove":
            title = input("Enter book title to remove: ").strip()
            manager.remove_book(title)
        elif command == "show":
            manager.show_books()
        elif command == "exit":
            break
        else:
            print("Invalid command. Please try again.")

if __name__ == "__main__":
    main()