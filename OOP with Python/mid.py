# 1. Library class
class Library:
    book_list = []

    @classmethod
    def entry_book(cls, book):
        cls.book_list.append(book)

    @classmethod
    def find_book_by_id(cls, book_id):
        for book in cls.book_list:
            if book._Book__book_id == book_id:
                return book
        return None


# 2. Book class
class Book:
    def __init__(self, book_id, title, author, availability=True):
        self.__book_id = book_id
        self.__title = title
        self.__author = author
        self.__availability = availability
        Library.entry_book(self)

    def borrow_book(self):
        if self.__availability:
            self.__availability = False
            print(f"The book '{self.__title}' has been borrowed.")
        else:
            print(f"Error: The book '{self.__title}' is already borrowed.")

    def return_book(self):
        if not self.__availability:
            self.__availability = True
            print(f"The book '{self.__title}' has been returned.")
        else:
            print(f"Error: The book '{self.__title}' was not borrowed.")

    def view_book_info(self):
        status = "Available" if self.__availability else "Not Available"
        print(
            f"Book id: {self.__book_id}, Title: {self.__title}, Author: {self.__author}, Availability: {status}"
        )


# 7. Menu System
def menu():
    while True:
        print("Library Menu")
        print("1. View All Books")
        print("2. Borrow Book")
        print("3. Return Book")
        print("4. Exit")

        user_input = input("Enter your option: ")

        if user_input == "1":
            print("\nList of Books:")
            for book in Library.book_list:
                book.view_book_info()

        elif user_input == "2":
            book_id = input("Enter Book ID: ")
            book = Library.find_book_by_id(book_id)
            if book:
                book.borrow_book()
            else:
                print(f"No book found{book_id}")

        elif user_input == "3":
            book_id = input("Enter Book id: ")
            book = Library.find_book_by_id(book_id)
            if book:
                book.return_book()
            else:
                print(f"No book found : {book_id}")

        elif user_input == "4":
            print("You Chosed Exit!! Programme breaked")
            break

        else:
            print("Something Wrong! Please enter a valid data.")


# 3. Add book objects
book1 = Book(1, "Harry Potter", "J.K. Rowling")
book2 = Book(2, "The Lord of the Rings", "J.R.R. Tolkien")
book3 = Book(3, "Pride and Prejudice", "Jane Austen")
book4 = Book(4, "The Great Gatsby", "F. Scott Fitzgerald")
book5 = Book(5, "To Kill a Mockingbird", "Harper Lee")
book6 = Book(6, "1984", "George Orwell")
book7 = Book(7, "Moby Dick", "Herman Melville")
book8 = Book(8, "The Catcher in the Rye", "J.D. Salinger")
book9 = Book(9, "The Hobbit", "J.R.R. Tolkien")
book10 = Book(10, "The Alchemist", "Paulo Coelho")

menu()
