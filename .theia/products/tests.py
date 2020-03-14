from django.test import TestCase
from .models import Product


# Create your tests here.
class ProductTests(TestCase):
    """
    Here we'll define tests tobe run against our
    Product model Methods. OBS! Has start with test!
    these test will ber run againtst the Product model
    """

    def test_str(self):
        test_name = Product(name='A product')
        self.assertEqual(str(test_name), 'A product')


"""
To run test: In theia terminal -write:
python3 manage.py test products
"""