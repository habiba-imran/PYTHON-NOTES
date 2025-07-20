# Write a Library class with no_of_books and books as two instance variables. Write a program to create 
# a library from this Library class and show how you can print all books, add a book and get the number 
# of books using different methods. Show that your program doesnt persist the books after the program 
# is stopped! 
class Library:
    def __init__(self, num, items):
        self.no_of_books = num
        self.books = items  # now using the passed list
    def add(self, item):
        self.books.append(item)
        self.no_of_books += 1
    def display(self):
        print("Books in library:", self.books)
    def remove(self, book_name):
        if book_name in self.books:
            self.books.remove(book_name)
            self.no_of_books -= 1
        else:
            print(f"'{book_name}' not found in library.")
    def display_number(self):
        print("Number of books:", self.no_of_books)
# Creating the library
a = Library(0, [])
# Adding books
a.add("Peer-e-Kamil")
a.add("Aab-e-Hayat")
# Display books and count
a.display()
a.display_number()
# Remove a book
a.remove("Aab-e-Hayat")
# Display again
a.display()
a.display_number()
