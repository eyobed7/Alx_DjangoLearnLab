>>> from bookshelf.models import Book
>>> 
>>> # Delete a Book
>>> book= Book.objects.get(id=1)
>>> book.delete()
(1, {'bookshelf.Book': 1})