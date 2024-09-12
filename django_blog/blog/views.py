from django.shortcuts import render,redirect,get_object_or_404
from django.urls import reverse,reverse_lazy
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
from .forms import UserUpdateForm, ProfileUpdateForm,CommentForm
from django.views.generic import DetailView,ListView,CreateView,UpdateView,DeleteView
from .models import Post,Comment
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin

class CommentCreateView(CreateView):
    model = Comment
    fields = ['content']
    template_name = 'blog/comment_form.html'

    def form_valid(self, form):
        post = get_object_or_404(Post, id=self.kwargs['post_id'])
        form.instance.post = post
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('post-detail', kwargs={'pk': self.kwargs['post_id']})

class CommentUpdateView(UpdateView):
    model = Comment
    fields = ['content']
    template_name = 'blog/comment_form.html'

    def get_success_url(self):
        return reverse_lazy('post-detail', kwargs={'pk': self.object.post.pk})

class CommentDeleteView(DeleteView):
    model = Comment
    template_name = 'blog/comment_confirm_delete.html'

    def get_success_url(self):
        return reverse_lazy('blog/post-detail', kwargs={'pk': self.object.post.pk})

class PostListView(ListView):
    model = Post
    template_name = 'blog/postlist.html'  # Template name for listing posts
    context_object_name = 'posts'


class PostCreateView(LoginRequiredMixin,CreateView):
    model = Post
    fields = ['title', 'content']  # Fields to be included in the form
    template_name = 'blog/postcreate.html'

    def form_valid(self, form):
        form.instance.author = self.request.user  # Set the author to the current user
        return super().form_valid(form)
    
class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']
    template_name = 'blog/post_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author  # Only allow the author to edit the 
    def get_success_url(self):
        # Assuming you have a profile view with a URL named 'profile'
        return reverse('postlist')  # Replace 'profile' with your actual URL name

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'blog/post_confirm_delete.html'

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author  # Only allow the author to delete the post
    def get_success_url(self):
        # Assuming you have a profile view with a URL named 'profile'
        return reverse_lazy('postlist')  # Replace 'profile' with your actual URL name
    
def register(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            return redirect('login')
    else:
        form = CreateUserForm()
    return render(request, 'blog/register.html', {'form': form})

def login(request):
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
    return render(request,'blog/login.html',{'loginform':form})

def logout_view(request):
    logout(request)
    return render(request, 'blog/logout.html')

@login_required()
def profile(request):
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.userprofile)
        comment_form=CommentForm(request.POST, instance=request.user)
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



