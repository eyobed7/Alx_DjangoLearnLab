from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import FileExtensionValidator


class CustomUser(AbstractUser):
    date_of_birth=models.DateField(null=True, blank=True) 
    profile_photo= models.ImageField(upload_to='profile_pictures/', null=True, blank=True, validators=[FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png'])])

class Book(models.Model):
    title=models.CharField(max_length=200)
    author=models.CharField(max_length=100)
    publication_year=models.IntegerField()

# Create your models here.
