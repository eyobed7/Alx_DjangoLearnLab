from django.db import models #Query all books by a specific author.
class Author(models.Model):
    name=models.CharField(max_length=15)


class Book (models.Model):
    title=models.CharField(max_length=15)
    author=models.ForeignKey(Author,on_delete=models.CASCADE,related_name='book')

class Library (models.Model):
    name=models.CharField(max_length=15)
    books=models.ManyToManyField(Book)

class Librarian (models.Model):
    name=models.CharField(max_length=15)
    library=models.OneToOneField(Library,on_delete=models.CASCADE,related_name='library')


