from models import Author,Book,Librarian,Library

# Assume you have an Author object
author = Author.objects.get(name="J.K. Rowling")

# Query all books by this author
books_by_author = Book.objects.filter(author=author)

# Print the titles of the books
for book in books_by_author:
    print(book.title)


# Assume you have a Library object
library = Library.objects.get(name="Central Library")

# Get all books in this library
books_in_library = library.books.all()

# Print the titles of the books
for book in books_in_library:
    print(book.title)
# Assume you have a Library object
library = Library.objects.get(name="Central Library")

# Retrieve the librarian for this library
librarian = library.librarian

# Print the librarian's name
print(librarian.name)
