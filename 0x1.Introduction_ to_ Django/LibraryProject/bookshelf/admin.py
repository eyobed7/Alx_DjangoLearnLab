from django.contrib import admin
from .models import Book

class BookAdmin(admin.ModelAdmin):
    # Display these fields in the admin list view
    list_display = ('title', 'author', 'publication_year')
    
    # Add search functionality for these fields
    search_fields = ('title', 'author')
    
    # Add filters based on these fields
    list_filter = ('author', 'publication_year')

# Register the Book model with the custom admin configuration
admin.site.register(Book, BookAdmin)
# Register your models here.
