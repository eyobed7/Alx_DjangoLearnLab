'''>>> from bookshelf.models import Book
>>> book = Book(title="strt with why",author="simion",publication_year=2020)
>>> book.save()

>>> from bookshelf.models import Book
>>> 
>>> # Retrieve all Book
>>> books = Book.objects.all()
>>> for book in books:
...     print(
...         book.title,
...         book.author,
...         book.publication_year
...         
...     )
...
strt with why simion 2020

>>> from bookshelf.models import Book
>>> 
>>> # Update a Book
>>> book = Book.objects.get(id=1)
>>> book.title = "start with why"
>>> book.save()


>>> from bookshelf.models import Book
>>> 
>>> # Delete a Book
>>> book= Book.objects.get(id=1)
>>> book.delete()
(1, {'bookshelf.Book': 1})

'''