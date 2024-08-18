# relationship_app/views.py

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import permission_required
from .models import Book

@permission_required('relationship_app.can_add_book')
def add_book(request):
    if request.method == 'POST':
        # Logic to add a book
        # Assuming you have a form to handle the book creation
        # Example: form = BookForm(request.POST)
        # if form.is_valid():
        #     form.save()
        return redirect('book_list')
    return render(request, 'relationship_app/add_book.html')

@permission_required('relationship_app.can_change_book')
def edit_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        # Logic to edit the book
        # Example: form = BookForm(request.POST, instance=book)
        # if form.is_valid():
        #     form.save()
        return redirect('book_list')
    return render(request, 'relationship_app/edit_book.html', {'book': book})

@permission_required('relationship_app.can_delete_book')
def delete_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        # Logic to delete the book
        book.delete()
        return redirect('book_list')
    return render(request, 'relationship_app/delete_book.html', {'book': book})

