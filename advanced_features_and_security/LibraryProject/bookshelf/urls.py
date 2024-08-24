from django.urls import path
from .views import book_list,homepage,register


urlpatterns = [
    path('',homepage,name='homepage'),
    path('register',register,name='register'),
    path('dashboard',book_list,name='dashboard'),
]