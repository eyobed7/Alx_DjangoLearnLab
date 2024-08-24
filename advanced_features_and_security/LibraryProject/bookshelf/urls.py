from django.urls import path
from .views import dashboard,homepage


urlpatterns = [
    path('',homepage,name='homepage'),
    path('dashboard',dashboard,name='dashboard'),
]