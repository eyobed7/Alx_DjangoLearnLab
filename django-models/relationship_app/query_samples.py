from relationship_app.models import Author, Book, Library, Librarian

def query_all_books_by_author(author_name):
    """Query all books by a specific author."""
    author = Author.objects.get(name=author_name)
    return Book.objects.filter(author=author)

def list_all_books_in_library(library_name):
    """List all books in a library."""
    library = Library.objects.get(name=library_name)
    return library.books.all()

def retrieve_librarian_for_library(library_name):
    """Retrieve the librarian for a library."""
    # Ensure this query follows the expected pattern:
    return Librarian.objects.get(library__name=library_name)
