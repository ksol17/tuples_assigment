# Task 1: Library System Enhancement 

library = [("1984", "George Orwell"), ("Brave New World", "Aldous Huxley")]

def add_book(library, title, author):
    new_book = (title, author)
    if new_book in library:
        print(f"The book '{title}' by {author}' already exists in the library.")
    else:
        library.append(new_book)
        print(f"The book '{title}' by {author} has been added to the library.")


add_book(library, "To Kill a Mockingbird", "Harper Lee")
add_book(library,"1984", "George Orwell")

print("Updated Library:", library)