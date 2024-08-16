from .views import list_books,LibraryDetailView,index
from django.urls import path,include

urlspattern=[
    path("", index, name="index"),
    path("booklist/",list_books , name="booklist"),
    path("listlibrary/", LibraryDetailView.as_view(), name="listlibrary"),


]