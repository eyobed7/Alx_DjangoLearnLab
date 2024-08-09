>>> from bookshelf.models import Book
>>> 
>>> # Update a Book
>>> book = Book.objects.get(id=1)
>>> book.title = "start with why"
>>> book.save()
