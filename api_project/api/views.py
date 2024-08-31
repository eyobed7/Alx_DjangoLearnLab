from rest_framework import viewsets 
from .models import Book
from .serializers import BookSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer  
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    # Corrected here
    def perform_create(self, serializer):
        # Custom logic for creating a comment (optional)
        serializer.save(user=self.request.user)

class MyAPIView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        # Only authenticated users can access this view
        return Response({'message': 'Hello, authenticated user!'})
