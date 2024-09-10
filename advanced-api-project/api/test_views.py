from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from .models import Book
from django.contrib.auth.models import User

from api.models import Book, Author  # Import the Author model

class BookAPITestCase(APITestCase):
    def setUp(self):
        # Create an Author instance
        self.client.login(username='testuser', password='testpassword')
        self.list_url = reverse('book-list')
        self.author = Author.objects.create(name='Author A')  # Adjust the field name as necessary
        
        # Create Book instances
        self.book1 = Book.objects.create(
            title='Book One', 
            publication_year='2020', 
            author=self.author  # Assign the Author instance here
        )
        self.book2 = Book.objects.create(
            title='Book Two', 
            publication_year='2021', 
            author=self.author  # Assign the Author instance here
        )
        
        # Create a User instance for testing authenticated access
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        
    def test_create_book(self):
       data = {'title': 'New Book', 'publication_year': '2022', 'author': 'Author D'}
       response = self.client.post(self.list_url, data)
       self.assertEqual(response.status_code, status.HTTP_201_CREATED)
       self.assertEqual(Book.objects.count(), 4)
       self.assertEqual(Book.objects.get(id=response.data['id']).title, 'New Book')

    def test_retrieve_book_list(self):
       response = self.client.get(self.list_url)
       self.assertEqual(response.status_code, status.HTTP_200_OK)
       self.assertEqual(len(response.data), 3)

    def test_retrieve_single_book(self):
        url = reverse('book-detail', args=[self.book1.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], self.book1.title)

    def test_update_book(self):
        url = reverse('book-detail', args=[self.book1.id])
        data = {'title': 'Updated Book Title'}
        response = self.client.patch(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book1.refresh_from_db()
        self.assertEqual(self.book1.title, 'Updated Book Title')

    def test_delete_book(self):
        url = reverse('book-detail', args=[self.book1.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 2)

    def test_search_books(self):
        response = self.client.get(self.list_url, {'search': 'Book One'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], 'Book One')

    def test_order_books_by_title(self):
        response = self.client.get(self.list_url, {'ordering': 'title'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['title'], 'Book One')  # Book One should be first alphabetically

    def test_access_denied_for_unauthenticated_users(self):
        self.client.logout()
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_access_granted_for_authenticated_users(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


