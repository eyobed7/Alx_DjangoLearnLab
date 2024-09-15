from django.shortcuts import render,redirect,get_object_or_404
from django.urls import reverse,reverse_lazy
from .forms import CreateUserForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.contrib.auth.models import auth
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import user_passes_test
from .forms import CreateUserForm,LoginForm,PostForm
from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import UserUpdateForm, ProfileUpdateForm,CommentForm
from django.views.generic import DetailView,ListView,CreateView,UpdateView,DeleteView
from .models import Post,Comment,Tag
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.db.models import Q

class CommentCreateView(CreateView):
    model = Comment
    fields = ['content']
    template_name = 'blog/comment_form.html'

    def form_valid(self, form):
        post = get_object_or_404(Post, id=self.kwargs['pk'])
        form.instance.post = post
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('post-detail', kwargs={'pk': self.kwargs['pk']})

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

def Post_search(request):
    query = request.GET.get('q')
    results = []
    if query:
        # Search by title, content, or tags
        results = Post.objects.filter(
            Q(title__icontains=query) |
            Q(content__icontains=query) |
            Q(tags__name__icontains=query)  # Assuming you have a tags field related to the Post model
        ).distinct()

    return render(request, 'blog/post_search.html', {'query': query, 'results': results})

class PostByTagListView(ListView):
    model = Post
    template_name = 'posts_by_tag.html'  # The template to render
    context_object_name = 'posts'  # The name of the context variable for the list of posts
    paginate_by = 10  # Optional: add pagination if necessary

    def get_queryset(self):
        # Get the tag based on the slug passed in the URL
        tag_slug = self.kwargs.get('tag_slug')
        tag = get_object_or_404(Tag, slug=tag_slug)
        
        # Return posts filtered by the tag
        return Post.objects.filter(tags=tag)

    def get_context_data(self, **kwargs):
        # Add additional context if needed (e.g., the current tag)
        context = super().get_context_data(**kwargs)
        context['tag'] = get_object_or_404(Tag, slug=self.kwargs.get('tag_slug'))
        return context

def posts_by_tag(request, tag_name):
    # Assuming you have a 'tags' field in your Post model or use a many-to-many relationship
    posts = Post.objects.filter(tags__name=tag_name)  # Adjust the filter based on your model's tag implementation
    return render(request, 'blog/posts_by_tag.html', {'posts': posts, 'tag_name': tag_name})

class PostCreateView(LoginRequiredMixin,CreateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/postcreate.html'

    def form_valid(self, form):
        form.instance.author = self.request.user  # Set the author to the current user
        return super().form_valid(form)
    def get_success_url(self):
        # Assuming you have a profile view with a URL named 'profile'
        return reverse('profile')  # Replace 'profile' with your actual URL name
    
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



