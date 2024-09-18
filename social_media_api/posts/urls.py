from .views import CommentViewSet,PostViewSet
from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import UserFeedView

# Create a router and register the viewsets
router = DefaultRouter()
router.register(r'posts', PostViewSet, basename='post')
router.register(r'comments',CommentViewSet, basename='comment')

urlpatterns = [
    path('poscom/', include(router.urls)),
    path('feed/', UserFeedView.as_view(), name='user-feed'),
   
]