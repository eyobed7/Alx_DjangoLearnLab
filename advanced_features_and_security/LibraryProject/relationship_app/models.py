from django.db import models
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from typing import Any
from django.db import models
from django.contrib.auth.models import AbstractUser,UserManager,PermissionsMixin
from django.utils import timezone
from django.core.validators import FileExtensionValidator

class CustomUserManger(UserManager):
    def _create_user(self,email,password,**extra_fields):
        if not email:
            raise ValueError("please insert your email")
        email=self.normalize_email(email)
        user=self.model(email=email,**extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    def create_user(self,email=None , password=None , **extra_fields) :
        extra_fields.setdefault("is_staff",False)
        extra_fields.setdefault("is_superuser",False)
        return self._create_user(email,password,**extra_fields)
    def create_superuser(self,email=None , password=None , **extra_fields) :
        extra_fields.setdefault("is_staff",True)
        extra_fields.setdefault("is_superuser",True)
        return self._create_user(email,password,**extra_fields)
    
class User(AbstractUser,PermissionsMixin):
    ROLE = [
        ('Admin', 'Admin'),
        ('MEMBER', 'MEMBER'),
        ('LIBRARY', 'LIBRARY'),
    ]
    role = models.CharField(max_length=24, choices=ROLE, default='MEMBER')
    email=models.EmailField(blank=True,unique=True,default='')
    name=models.CharField(max_length=255,blank=True,default='')
    date_of_birth=models.DateField(null=True, blank=True) 
    profile_photo= models.ImageField(upload_to='profile_pictures/', null=True, blank=True, validators=[FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png'])])


    is_active=models.BooleanField(default=True)
    is_staff=models.BooleanField(default=False)
    is_superuser=models.BooleanField(default=False)

    datajoined=models.DateTimeField(default=timezone.now)
    objects=CustomUserManger()
    USERNAME_FIELD="email"
    EMAIL_FIELD="email"
    REQUIRED_FIELDS=[]
    
class UserProfile(models.Model):
    ROLE_CHOICES = [
        ('Admin', 'Admin'),
        ('Librarian', 'Librarian'),
        ('Member', 'Member'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)

    def __str__(self):
        return f'{self.user.username} - {self.role}'


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.userprofile.save()

class Author(models.Model):
    name = models.CharField(max_length=15)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=15)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')

    class Meta:
        permissions = [
            ("can_add_book", "Can add book"),
            ("can_change_book", "Can change book"),
            ("can_delete_book", "Can delete book"),
        ]

    def __str__(self):
        return self.title


class Library(models.Model):
    name = models.CharField(max_length=15)
    books = models.ManyToManyField(Book)

    def __str__(self):
        return self.name


class Librarian(models.Model):
    name = models.CharField(max_length=15)
    library = models.OneToOneField(Library, on_delete=models.CASCADE, related_name='librarian')

    def __str__(self):
        return f"{self.name}, Librarian at {self.library.name}"
