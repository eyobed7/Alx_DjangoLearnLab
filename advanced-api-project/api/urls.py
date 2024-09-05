from django.urls import path
from .views import BookListCreateAPIView,AuthorListCreateAPIView

urlpatterns = [
    path("api/books", BookListCreateAPIView.as_view(), name="book_list_create"),
    path("api/Authors", AuthorListCreateAPIView.as_view(), name="author_list_create"),
]