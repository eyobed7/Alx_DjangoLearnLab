from .views import CommentViewSet,PostViewSet
from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import UserFeedView
from .views import like_post, unlike_post


# Create a router and register the viewsets
router = DefaultRouter()
router.register(r'posts', PostViewSet, basename='post')
router.register(r'comments',CommentViewSet, basename='comment')

urlpatterns = [
    path('poscom/', include(router.urls)),
    path('feed/', UserFeedView.as_view(), name='user-feed'),
    path('posts/<int:pk>/like/', like_post, name='like_post'),
    path('posts/<int:pk>/unlike/', unlike_post, name='unlike_post'),
   
]