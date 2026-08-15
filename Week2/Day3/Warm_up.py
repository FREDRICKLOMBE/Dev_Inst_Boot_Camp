"""  PERSONAL LIBRARY    """
#Create a class named Book
class Book:
    def __init__(self, title, author = None):
        self.title = title
        self.author = author
        self.is_home = True

#Get information about the book

    def get_info(self):
        # title = input("Enter Book Title: ")
        # author = input("Enter Book Author: ")
        if self.is_home:
            book_status = "Home"

        else:
            book_status = "Book is lent to someone"
        return (f"Book Title: {self.title.title()} and Author: {self.author.title()}"
                f"\nStatus: {book_status}")

book1 = Book("Harry Potter", "Fred")
print(book1.get_info())

    def create_a_library():
        while True:
            current = input("Enter a book title or exit to quit: ")
            if current == "exit":
                break
            

#Lend 2 books to someone and show the library again.
book_library = {
    "J.R.R. Tolkien" : "The Hobbit",

    "Jane Austen" : [ "Emma", "Persuasion"],

    "George Orwell": ["1984", "Animal Farm"],

    "Agatha Christie": [
        "And Then There Were None",
        "Murder on the Orient Express"
    ],
    "Chinua Achebe" : [
        "Things fall apart",
        "No longer at ease"
        ],

    "Stephen King": [
        "The Shining",
        "The Stand",
    ],
    "Isaac Asimov": "Foundation",
}



