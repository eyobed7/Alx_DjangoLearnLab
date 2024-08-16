from .views import list_books,LibraryDetailView,index,CustomLoginView, product
from django.urls import path
from django.contrib.auth.views import LogoutView

urlspattern=[
    path("", index, name="index"),
    path("booklist/",list_books , name="booklist"),
    path("listlibrary/", LibraryDetailView.as_view(), name="listlibrary"),
    path("register/", register, name="register"),
    path("login/", CustomLoginView.as_view(next_page="product"), name="login"),
    path("product/", product, name="product"),
    path("logout/", LogoutView.as_view(next_page="index"), name="logout"),

]
from django.urls import path
from .views import index, register, CustomLoginView, product



