from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import permission_required


def homepage(request):
    return render(request,'bookshelf/homepage.html')

@permission_required('bookshelf.can_edit', raise_exception=True)
def book_list(request):
    return render(request,'bookshelf/dashboard.html')

