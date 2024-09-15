from django.urls import path
from .views import register,PostByTagListView,logout_view,profile,login,Post_search,PostListView,PostCreateView,PostDetailView,PostUpdateView,PostDeleteView,CommentCreateView,CommentUpdateView,CommentDeleteView
from django.contrib.auth.views import LoginView



urlpatterns = [
    path('register/', register, name='register'),
    path('post/new/', PostCreateView.as_view(), name='postcreate'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('postlist/', PostListView.as_view(), name='postlist'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('login/',login,name='login'),
    path('search/', Post_search, name='post-search'),
    path('logout/', logout_view, name='logout'),
    path('profile/', profile, name='profile'),
    path('tags/<slug:tag_slug>/', PostByTagListView.as_view(), name='posts_by_tag'),
    path('post/<int:pk>/comments/new/', CommentCreateView.as_view(), name='comment-create'),
    path('comment/<int:pk>/update/', CommentUpdateView.as_view(), name='comment-edit'),
    path('comment/<int:pk>/delete/', CommentDeleteView.as_view(), name='comment-delete'),
]

