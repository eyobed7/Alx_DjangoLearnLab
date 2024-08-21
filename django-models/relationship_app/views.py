from django.shortcuts import render,redirect
from .models import Library,Book
from django.views.generic.detail import DetailView
from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            return redirect('my_login')
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})


# Login view
class CustomLoginView(LoginView):
    template_name = 'relationship_app/login.html'

# Logout view
class CustomLogoutView(LogoutView):
    template_name = 'relationship_app/logout.html'


def is_admin(user):
    return user.userprofile.role == 'Admin'

def is_librarian(user):
    return user.userprofile.role == 'Librarian'

def is_member(user):
    return user.userprofile.role == 'Member'

@user_passes_test(is_admin)
def admin_view(request):
    return render("relationship_app/admin_view.html")

@user_passes_test(is_librarian)
def librarian_view(request):
    return render("relationship_app/librarian_view.html")

@user_passes_test(is_member)
def member_view(request):
    return render("relationship_app/member_view.html")


def list_books(request):
    books = Book.objects.all()  # Query all books from the database
    return render(request, 'relationship_app/list_books.html', {'books': books})



class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'

