from django.shortcuts import render
from django.views.generic import DetailView
from .models import Library,Book

def book_list(request):
      """Retrieves all books and renders a template displaying the list."""
      boo = Book.objects.all()  # Fetch all book instances from the database
      context = {'books': boo}  # Create a context dictionary with book list
      return render(request,'list_books.html', context)
# Create your views here.

class bookListView(DetailView):
    model = Library
    template_name = 'library_detail.html'
    context_object_name = 'library'

def index(request):
    return render(request, "index.html")
