from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views
from django.urls import path
from .views import add_book, edit_book, delete_book, list_books, LibraryDetailView

urlpatterns = [
    # Book-related URLs
    
    path('add_book/', add_book, name='add_book'),  # Add a new book
    path('edit_book/<int:pk>/', edit_book, name='edit_book'),  # Edit an existing book
    path('delete_book/<int:pk>/', delete_book, name='delete_book'),  # Delete a book
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
    path('register/', views.register, name='register'),
    
    # Library-related URL (example)
    path('libraries/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
]


'''path('books/', list_books, name='list_books'),
    path('library/', LibraryDetailView.as_view(), name='library_detail'),'''