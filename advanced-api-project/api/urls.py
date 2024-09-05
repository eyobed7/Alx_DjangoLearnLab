from django.urls import path
from .views import BookList, BookDetail, BookCreate, BookUpdate, BookDelete,BookListCreateAPIView,AuthorListCreateAPIView

urlpatterns = [
    path('books/', BookList.as_view(), name='book-list'),
    path('books/<int:pk>/', BookDetail.as_view(), name='book-detail'),
    path('books/create/', BookCreate.as_view(), name='book-create'),
    path('books/update/<int:pk>/', BookUpdate.as_view(), name='book-update'),
    path('books/delete/<int:pk>/', BookDelete.as_view(), name='book-delete'),
    path("api/books", BookListCreateAPIView.as_view(), name="book_list_create"),
    path("api/Authors", AuthorListCreateAPIView.as_view(), name="author_list_create"),
]
