from django.shortcuts import render,redirect
from .forms import CreateUserForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.contrib.auth.models import auth
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import user_passes_test
from .forms import CreateUserForm,LoginForm
from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import UserUpdateForm, ProfileUpdateForm

def register(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            return redirect('my_login')
    else:
        form = CreateUserForm()
    return render(request, 'blog/register.html', {'form': form})

def my_login(request):
    form=LoginForm()
    if request.method == 'POST':
        form=LoginForm(request,data=request.POST)
        if form.is_valid():
            username=request.POST.get('username')
            password=request.POST.get('password')
            user=authenticate(request,username=username,password=password)
            
            if user is not None:
                auth.login(request,user)
                return redirect("profile")
            else:
                messages.error(request, "Invalid credentials or account inactive")
    return render(request,'blog/my_login.html',{'loginform':form})

def logout_view(request):
    logout(request)
    return render(request, 'blog/logout.html')

@login_required()
def profile(request):
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.userprofile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('profile')
    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.userprofile)

    context = {
        'user_form': user_form,
        'profile_form': profile_form
    }

    return render(request, 'blog/profile.html', context)



