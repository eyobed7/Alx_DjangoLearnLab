from django.urls import path
from .views import register,logout_view,profile,login
from django.contrib.auth.views import LoginView



urlpatterns = [
    path('register/', register, name='register'),
    path('login/',login,name='login'),
    path('logout/', logout_view, name='logout'),
    path('profile/', profile, name='profile'),
    # Add other URL patterns here
]