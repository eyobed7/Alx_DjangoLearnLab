from rest_framework.authtoken.views import obtain_auth_token
from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import BookViewSet,BookList # Ensure this import is correct
router = DefaultRouter()
router.register(r'books', BookViewSet)

'''router = DefaultRouter()
router.register(r'cohort', BookViewSet, basename='cohort')'''

urlpatterns = [
    # Other URL patterns
    path('', include(router.urls)),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
    path('books/', BookList.as_view(), name='book-list'),

]
