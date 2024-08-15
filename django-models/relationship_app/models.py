from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=15)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=15)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')

    def __str__(self):
        return self.title

class Library(models.Model):
    name = models.CharField(max_length=15)
    books = models.ManyToManyField(Book)

    def __str__(self):
        return self.name

class Librarian(models.Model):
    name = models.CharField(max_length=15)
    library = models.OneToOneField(Library, on_delete=models.CASCADE, related_name='librarian')

    def __str__(self):
        return self.name
