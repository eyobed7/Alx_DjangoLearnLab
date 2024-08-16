from .views import list_books,LibraryDetailView,index,CustomLoginView, product
from django.urls import path
from django.contrib.auth.views import LogoutView
from django.urls import path
from .views import index, register, LoginView, product

urlspattern=[
    path("", index, name="index"),
    path("login/", CustomLoginView.as_view('login.html'), name="login"),
    path("logout/", LogoutView.as_view('logout.html'), name="logout"),
    path("booklist/",list_books , name="booklist"),
    path("listlibrary/", LibraryDetailView.as_view(), name="listlibrary"),
    path("register/", register, name="register"),  
    path("product/", product, name="product"),
    
]




