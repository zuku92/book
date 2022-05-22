from django.test import TestCase
from store.logic import operations

class LogicTestCase(TestCase):

    def test_plus(self):
        result = operations(4, 7, '+')
        self.assertEqual(11, result)

    def test_minus(self):
        result = operations(33, 3, '-')
        self.assertEqual(30, result)

    def test_multiply(self):
        result = operations(11, 3, '*')
        self.assertEqual(33, result)

