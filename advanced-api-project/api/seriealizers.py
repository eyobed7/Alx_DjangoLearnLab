from rest_framework import serializers
from .models import Book,Author
from datetime import datetime

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model=Book
        fields = '__all__'
    def validate(self, data):
        current_year = datetime.now().year
        if data['publication_year'] > current_year:
            raise serializers.ValidationError("The publication year cannot be in the future.")
        return data
    

class AuthorSerializer(serializers.ModelSerializer):
    authors=BookSerializer(many=True, read_only=True)
    class Meta:
        model=Author
        fields=['name','authors']

   