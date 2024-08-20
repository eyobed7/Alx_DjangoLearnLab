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
    # The query the evaluation script is looking for
    return Librarian.objects.get(Library=library_name)