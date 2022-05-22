from django.test import TestCase

from store.models import Book
from store.serializers import BooksSerializer


class BookSerializersTestCase(TestCase):
    def test_ok(self):

        book1 = Book.objects.create(name='testbook_1', price='12.30', author_name='author_1')
        book2 = Book.objects.create(name='testbook_2', price='17.30', author_name='author_2')
        data = BooksSerializer([book1, book2], many=True).data

        expected_data = [

            {
                'id': book1.id,
                'name':'testbook_1',
                'price': '12.30',
                'author_name':'author_1',
            },

            {
                'id': book2.id,
                'name': 'testbook_2',
                'price': '17.30',
                'author_name': 'author_2',
            }

        ]

        self.assertEqual(expected_data, data)

