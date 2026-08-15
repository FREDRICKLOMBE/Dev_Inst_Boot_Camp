class Genre():
    def __init__(self, name, books = None):
        self.name = name
        self.books = books

    def get_books(self):
        """Return the list of books belonging to this genre."""
        return self.books

    def get_name(self):
        """Return the name of the genre."""
        return self.name

    def show_info(self):
        """Print a summary of the genre and its books."""
        print(f"Genre: {self.name}")
        if self.books:
            print("Books:")
            for book in self.books:
                print(f"  - {book}")
        else:
            print("No books in this genre yet.")

buk = ['Twilight', "Originals", "Vampire Diaries", "Blade"]

view1 = Genre("Fantasy", buk)
view1.show_info()

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