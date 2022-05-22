from rest_framework.test import APITestCase
from django.urls import reverse

from store.models import Book
from store.serializers import BooksSerializer
from rest_framework import status


class BooksApiTestCase(APITestCase):

    def test_get(self):

        book1 = Book.objects.create(name='testbook_1', price='12.30', author_name='author_1')
        book2 = Book.objects.create(name='testbook_2', price='17.30', author_name='author_2')

        url = reverse('book-list')
        responce = self.client.get(url)

        self.assertEqual(status.HTTP_200_OK, responce.status_code)
        serializer_data =BooksSerializer([book1, book2], many=True).data
        self.assertEqual(serializer_data, responce.data)


