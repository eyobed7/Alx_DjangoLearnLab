from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.detail import DetailView
from .models import Library,Book
from django.shortcuts import render, redirect
from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponseForbidden

def is_admin(user):
    return user.userprofile.role == 'Admin'

def is_librarian(user):
    return user.userprofile.role == 'Librarian'

def is_member(user):
    return user.userprofile.role == 'Member'

@user_passes_test(is_admin)
def admin_view(request):
    return render(request, 'admin_view.html')

@user_passes_test(is_librarian)
def librarian_view(request):
    return render(request, 'librarian_view.html')

@user_passes_test(is_member)
def member_view(request):
    return render(request, 'member_view.html')

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
