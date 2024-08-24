from django.urls import path
from .views import book_list,homepage


urlpatterns = [
    path('',homepage,name='homepage'),
    path('dashboard',book_list,name='dashboard'),
]