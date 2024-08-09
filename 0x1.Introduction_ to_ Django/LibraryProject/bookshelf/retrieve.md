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