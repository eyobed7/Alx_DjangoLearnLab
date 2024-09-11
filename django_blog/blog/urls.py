from django.urls import path
from .views import register,logout_view,profile,login,PostListView,PostCreateView,PostDetailView,PostUpdateView,PostDeleteView
from django.contrib.auth.views import LoginView



urlpatterns = [
    path('register/', register, name='register'),
    path('postcreate/new/', PostCreateView.as_view(), name='postcreate'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('postlist/', PostListView.as_view(), name='postlist'),
    path('post/<int:pk>/edit/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('login/',login,name='login'),
    path('logout/', logout_view, name='logout'),
    path('profile/', profile, name='profile'),
    # Add other URL patterns here
]