from rest_framework.authtoken.views import obtain_auth_token
from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import BookViewSet # Ensure this import is correct

'''router = DefaultRouter()
router.register(r'cohort', BookViewSet, basename='cohort')'''

urlpatterns = [
    # Other URL patterns
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),

]
