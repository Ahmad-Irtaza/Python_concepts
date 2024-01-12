library = {}

def add_book(title, author, year):
    """Add a new book to the library."""
    if title not in library:
        library[title] = {'Author': author, 'Year': year}
        print(f"Book '{title}' added to the library.")
    else:
        print(f"Book '{title}' is already in the library.")

def search_book(title):
    """Search for a book by title."""
    if title in library:
        print(f"Book '{title}' found in the library:")
        print(f"Author: {library[title]['Author']}")
        print(f"Year: {library[title]['Year']}")
    else:
        print(f"Book '{title}' not found in the library.")

def display_library():
    """Display all books in the library."""
    if not library:
        print("The library is empty.")
    else:
        print("Books in the library:")
        for title, info in library.items():
            print(f"Title: {title}, Author: {info['Author']}, Year: {info['Year']}")

add_book("Peer-e-kamil", "F. umera", 1925)
add_book("Atomic habit", "james", 1960)
add_book("1984", "George Orwell", 1949)

search_book("Atomic habit")
search_book("Peer-e-kamail")

display_library()
