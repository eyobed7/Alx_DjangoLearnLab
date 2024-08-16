from .views import book_list,index,LibraryDetailView
from django.urls import path,include

urlspattern=[
    path("", index, name="index"),
    path("booklist/",book_list , name="booklist"),
    path("listlibrary/", LibraryDetailView.as_view(), name="listlibrary"),


]