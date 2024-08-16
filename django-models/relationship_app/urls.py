from .views import book_list,index,bookListView
from django.urls import path,include

urlspattern=[
    path("", index, name="index"),
    path("booklist/",book_list , name="booklist"),
    path("listlibrary/", bookListView.as_view(), name="listlibrary"),


]