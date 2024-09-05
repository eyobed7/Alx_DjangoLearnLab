from rest_framework import generics
from .models import Book,Author
from .seriealizers import AuthorSerializer,BookSerializer
from rest_framework import permissions

class IsAdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        # Only allow non-admins to perform safe methods (GET, HEAD, OPTIONS)
        if request.method in permissions.SAFE_METHODS:
            return True
        # Only allow admin users to create, update, or delete
        return request.user and request.user.is_staff

class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]
    
class BookDetail(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]
     
class BookCreate(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAdminOrReadOnly]

    def perform_create(self, serializer):
        if serializer.validated_data['publication_year'] > 2024:
            raise serializer.ValidationError("Publication year cannot be in the future.")
        serializer.save(author=self.request.user)

class BookUpdate(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_update(self, serializer):
        # Ensure the user updating the book is the author
        if serializer.instance.author != self.request.user:
            raise serializer.ValidationError("You are not the author of this book.")
        if serializer.validated_data['publication_year'] > 2024:
            raise serializer.ValidationError("Publication year cannot be in the future.")
        serializer.save()
    

class BookDelete(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]



class BookListCreateAPIView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class AuthorListCreateAPIView(generics.ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer    