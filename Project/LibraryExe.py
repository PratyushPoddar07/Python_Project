class Library:
    def __init__(self):
        self.noBooks = 0
        self.books = {}

    def print_books(self):
        if self.noBooks == 0:
            print("No books in the library.")
        else:
            print("Books in the library: ")
            for book, category in self.books.items():
                print(f"- {book} (Category: {category})")

    def add_books(self, book, category):
        self.books[book] = category
        self.noBooks += 1
        print(f"'{book}' has been added to the library.")

    def remove_book(self, book):
        if book in self.books:
            del self.books[book]
            self.noBooks -= 1
            print(f"'{book}' has been removed from the library.")
        else:
            print(f"'{book}' is not found in the library!")

    def get_noBooks(self):
        return self.noBooks


# Main program loop
l2 = Library()

while True:
    print("\nOptions:")
    print("1. Add a book")
    print("2. Remove a book")
    print("3. Print all books")
    print("4. Get the number of books")
    print("5. Exit")
    
    choice = input("Enter your choice (1-5): ")

    if choice == '1':
        book = input("Enter the book name: ")
        category = input("Enter the category of the book: ")
        l2.add_books(book, category)
    
    elif choice == '2':
        book = input("Enter the book name to remove: ")
        l2.remove_book(book)

    elif choice == '3':
        l2.print_books()

    elif choice == '4':
        print("Number of books in the library:", l2.get_noBooks())
    
    elif choice == '5':
        print("Exiting the program.")
        break

    else:
        print("Invalid choice! Please enter a number between 1 and 5.")

