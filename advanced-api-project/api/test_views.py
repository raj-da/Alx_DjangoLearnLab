from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import Book
from django.contrib.auth.models import User

class BookAPITestCase(TestCase):
    def setUp(self):

        self.client - APIClient()

        self.client.login(username="test_user", password="test_password")

        self.book1 = Book.objects.create(title = "First Book", author="Author 1", publication_year=1996)
        self.book2 = Book.objects.create(title = "Second Book", author="Author 2", publication_year=1997)
        self.book3 = Book.objects.create(title = "3rd Book", author="Author 1", publication_year=2000)

    def test_list_books(self):
        response = self.client.get('/api/books/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 3) # ensures all books are returned

    def test_create_book(self):
        data = {"title" : "4th Book", "author" : "Author 3", "publication_year" : 2007}
        response = self.client.post('/api/books/', data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Book.objects.count(), 4)
        self.assertEqual(Book.objects.last().title, "4th Book")
    
    def test_update_book(self):
        data = {"title" : "Updated First Book Fitle"}
        response = self.client.patch(f'/api/books/{self.book1.id}', data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book1.refresh_from_db()
        self.assertEqual(self.book1.title, "Updated First Book Title")

    def test_delete_book(self):
        response = self.client.delete(f'/api/books/{self.book1.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 2)