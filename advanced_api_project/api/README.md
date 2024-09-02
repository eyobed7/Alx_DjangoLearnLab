To fulfill the documentation requirements, you can add detailed comments in the `models.py` and `serializers.py` files. These comments will explain the purpose of each model and serializer and describe how the relationship between `Author` and `Book` is handled.

### `models.py` with Detailed Comments

```python
from django.db import models

# The Author model represents an author in the system.
# It includes a 'name' field to store the author's name.
class Author(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

# The Book model represents a book in the system.
# It includes a 'title' field for the book's title,
# a 'publication_year' field for the year the book was published,
# and a foreign key 'author' that links the book to its author.
# The relationship between Author and Book is one-to-many,
# meaning an author can have multiple books.
class Book(models.Model):
    title = models.CharField(max_length=255)
    publication_year = models.IntegerField()
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)

    def __str__(self):
        return self.title
```

### `serializers.py` with Detailed Comments

```python
from rest_framework import serializers
from .models import Author, Book
from datetime import datetime

# The BookSerializer handles the serialization and deserialization of Book objects.
# It includes all fields of the Book model and performs custom validation on the
# 'publication_year' field to ensure that the publication year is not in the future.
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

    # Custom validation to ensure the publication year is not in the future.
    def validate(self, data):
        current_year = datetime.now().year
        if data['publication_year'] > current_year:
            raise serializers.ValidationError("The publication year cannot be in the future.")
        return data

# The AuthorSerializer handles the serialization and deserialization of Author objects.
# It includes the 'name' field and uses a nested BookSerializer to serialize the
# related books dynamically. This means that when an Author object is serialized,
# the related books are also included as a nested list of serialized Book objects.
class AuthorSerializer(serializers.ModelSerializer):
    # The 'books' field is a nested serializer that serializes the related Book objects.
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ['name', 'books']

    # Relationship handling:
    # The AuthorSerializer uses a nested BookSerializer to serialize the books related to the author.
    # This establishes a one-to-many relationship between Author and Book in the serializer,
    # ensuring that when an Author object is serialized, all related Book objects are included in the output.
```

### Explanation:

1. **Models Explanation:**
   - **Author Model:** Represents an author in the system, with a `name` field to store the author's name.
   - **Book Model:** Represents a book with a `title`, `publication_year`, and a foreign key `author` linking it to an `Author`. The relationship between `Author` and `Book` is one-to-many, meaning that an author can have multiple books.

2. **Serializers Explanation:**
   - **BookSerializer:** Handles serialization of the `Book` model, including a custom validation method that ensures the `publication_year` is not in the future.
   - **AuthorSerializer:** Serializes the `Author` model and includes a nested `BookSerializer` to serialize related books. This means that when an author is serialized, all of their related books are also included in the output as a nested list. This handles the one-to-many relationship between `Author` and `Book` in the serialization process.

These comments will help other developers understand the purpose and functionality of the models and serializers, as well as how relationships are handled in the serialization process.