from rest_framework import viewsets 
from .models import Book
from .serializers import BookSerializer

class BookViewSet(viewsets.ViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer  # Corrected here
