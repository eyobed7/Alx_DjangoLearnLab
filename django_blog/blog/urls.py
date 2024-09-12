from django.urls import path
from .views import register,logout_view,profile,login,PostListView,PostCreateView,PostDetailView,PostUpdateView,PostDeleteView,CommentCreateView,CommentUpdateView,CommentDeleteView
from django.contrib.auth.views import LoginView



urlpatterns = [
    path('register/', register, name='register'),
    path('post/new/', PostCreateView.as_view(), name='postcreate'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('postlist/', PostListView.as_view(), name='postlist'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('login/',login,name='login'),
    path('logout/', logout_view, name='logout'),
    path('profile/', profile, name='profile'),
    path('posts/<int:post_id>/comments/new/', CommentCreateView.as_view(), name='comment-create'),
    path('comments/<int:pk>/edit/', CommentUpdateView.as_view(), name='comment-edit'),
    path('comments/<int:pk>/delete/', CommentDeleteView.as_view(), name='comment-delete'),
]
