from .models import Author,Book,Librarian,Library

# Assuming you have an author instance
author = Author.objects.get(id=1)  # Replace `author_id` with the actual ID
# Query all books by this author
books_by_author = Book.objects.filter(author=author)


# Alternatively, if you have the author's name:
books_by_author = Book.objects.filter(author__name="Author Name")
# Assuming you have a library instance
library = Library.objects.get(id=1)  # Replace `library_id` with the actual ID

# List all books in this library
books_in_library = library.books.all()

# Assuming you have a library instance
library = Library.objects.get(id=1)  # Replace `library_id` with the actual ID

# Retrieve the librarian for this library
librarian = library.library
