from django.urls import path,include
from .views import RegisterView,LoginView ,ProfileView,CommentViewSet,PostViewSet
from rest_framework.routers import DefaultRouter

# Create a router and register the viewsets
router = DefaultRouter()
router.register(r'posts', PostViewSet, basename='post')
router.register(r'comments',CommentViewSet, basename='comment')



urlpatterns = [
    path('poscom/', include(router.urls)),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('profile/', ProfileView.as_view(), name='profile'),
]

