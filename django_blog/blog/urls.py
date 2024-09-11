from django.urls import path
from .views import register,logout_view,profile,my_login
from django.contrib.auth.views import LoginView



urlpatterns = [
    path('register/', register, name='register'),
    path('my_login/',my_login,name='my_login'),
    path('logout/', logout_view, name='logout'),
    path('profile/', profile, name='profile'),
    # Add other URL patterns here
]