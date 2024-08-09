from bookshelf.models import Book

# Retrieve a single Book by a specific field, e.g., title
book = Book.objects.get(title="1984")
print(
    book.title,
    book.author,
    book.publication_year
)

1984 George Orwell 1949