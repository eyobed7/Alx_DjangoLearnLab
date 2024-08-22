from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import permission_required
from .models import Library,Book
from django.views.generic.detail import DetailView
from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required

@permission_required('relationship_app.can_add_book')
def add_book(request):
    if request.method == "POST":
        title = request.POST.get('title')
        author_id = request.POST.get('author')  # Assume author is selected by ID
        publication_year = request.POST.get('publication_year')

        if title and author_id:
            Book.objects.create(
                title=title,
                author_id=author_id,
                publication_year=publication_year
            )
            return redirect('book_list')
    return render(request, 'relationship_app/add_book.html')

@permission_required('relationship_app.can_change_book')
def edit_book(request, pk):
    book = get_object_or_404(Book, pk=pk)

    if request.method == "POST":
        book.title = request.POST.get('title', book.title)
        book.author_id = request.POST.get('author', book.author_id)
        book.publication_year = request.POST.get('publication_year', book.publication_year)
        book.save()
        return redirect('book_detail', pk=book.pk)

    return render(request, 'relationship_app/edit_book.html', {'book': book})

@permission_required('relationship_app.can_delete_book')
def delete_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == "POST":
        book.delete()
        return redirect('book_list')
    return render(request, 'relationship_app/delete_book.html', {'book': book})
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
''''def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'relationship_app/login.html', {'form': form})

# Logout view
def user_logout(request):
    logout(request)
    return redirect('login')'''


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

