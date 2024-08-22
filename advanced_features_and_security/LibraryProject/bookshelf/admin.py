from django.contrib import admin
from .models import Book,CustomUser
from django.contrib.auth.admin import UserAdmin

class CustomUserAdmin(UserAdmin):
    pass


class BookAdmin(admin.ModelAdmin):
    # Display these fields in the admin list view
    list_display = ('title', 'author', 'publication_year')
    
    # Add search functionality for these fields
    search_fields = ('title', 'author')
    
    # Add filters based on these fields
    list_filter = ('author', 'publication_year')

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Book, BookAdmin)

# Register your models here.
