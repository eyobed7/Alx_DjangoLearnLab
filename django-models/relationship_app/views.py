from django.views.generic.detail import DetailView
from django.shortcuts import render
from .models import Library,Book

def list_books(request):
      """Retrieves all books and renders a template displaying the list."""
      boo = Book.objects.all()  # Fetch all book instances from the database
      context = {'books': boo}  # Create a context dictionary with book list
      return render(request,'relationship_app/list_books.html', context)
# Create your views here.

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'

def index(request):
    return render(request, "relationship_app/index.html")
