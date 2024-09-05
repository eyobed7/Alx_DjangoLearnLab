from rest_framework import generics
from .models import Book,Author
from .seriealizers import AuthorSerializer,BookSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework import permissions


class IsAdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        # Only allow non-admins to perform safe methods (GET, HEAD, OPTIONS)
        if request.method in permissions.SAFE_METHODS:
            return True
        # Only allow admin users to create, update, or delete
        return request.user and request.user.is_staff

# ListAPIView: Handles retrieving a list of books (similar to ListView)
class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]  # Only authenticated users can modify, anyone can view

# RetrieveAPIView: Handles retrieving a single book by ID (similar to DetailView)
class BookDetail(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]  # Only authenticated users can modify, anyone can view

# CreateAPIView: Handles creating a new book (similar to CreateView)
class BookCreate(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]  # Only authenticated users can create

# UpdateAPIView: Handles updating an existing book (similar to UpdateView)
class BookUpdate(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]  # Only authenticated users can update

# DestroyAPIView: Handles deleting a book (similar to DeleteView)
class BookDelete(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]  # Only authenticated users can delete



class BookListCreateAPIView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class AuthorListCreateAPIView(generics.ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer    

''' '''