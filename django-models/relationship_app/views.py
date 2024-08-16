from django.views.generic.detail import DetailView
from .models import Library,Book
from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form = UserCreationForm()

    return render(request, "relationship_app/register.html", {"form": form})

class CustomLoginView(LoginView):
    template_name = "relationship_app/login.html"

def product(request):
    return render(request, "relationship_app/product.html")

def index(request):
    return render(request, "relationship_app/index.html")
def product(request):
    return render(request, "product.html")

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
