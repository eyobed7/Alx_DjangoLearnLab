from rest_framework import serializers
from .models import  Book


class BookSerializer(serializers.ModelSerializer):
    # Nesting AuthorSerializer within BookSerializer
    class Meta:
        model = Book
        fields = '__all__'


