from .views import list_books,LibraryDetailView,index,CustomLoginView, product
from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from .views import index, register
from . import views

urlspattern=[
    path('register/', views.register, name='register'),  # views.register for user registration
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),  # Custom LoginView
    path('logout/', LogoutView.as_view(template_name='relationship_app/logged_out.html'), name='logout'),
    path("", index, name="index"),
    path("booklist/",list_books , name="booklist"),
    path("listlibrary/", LibraryDetailView.as_view(), name="listlibrary"), 
    path("product/", product, name="product"),
    
]







