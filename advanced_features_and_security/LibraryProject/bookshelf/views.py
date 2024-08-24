from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.models import Group
from .forms import CustomUserCreationForm

def register(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            role = form.cleaned_data.get("role")
            if role == "creator":
                creator_group = Group.objects.get(name="Editors")
                user.groups.add(creator_group)
            elif role == "reader":
                creator_group = Group.objects.get(name="Viewers")
                user.groups.add(creator_group)
        
            return redirect("homepage")
    else:
        form = CustomUserCreationForm()
    return render(request, "bookshelf/Example.html", {"form": form})
        
def homepage(request):
    return render(request,'bookshelf/homepage.html')

@permission_required('bookshelf.can_edit', raise_exception=True)
def book_list(request):
    return render(request,'bookshelf/dashboard.html')

