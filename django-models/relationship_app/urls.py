from django.urls import path
import views #import list_books, LibraryDetailView,user_login, register,user_logout
from.views import list_books, LibraryDetailView

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('books/', list_books, name='list_books'),
    path('library/', LibraryDetailView.as_view(), name='library_detail'),
]
