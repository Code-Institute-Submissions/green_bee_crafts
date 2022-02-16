from django.test import TestCase

from django.urls import reverse, resolve
from django.shortcuts import get_object_or_404

from products.models import Product, Category
from .views import view_bag, add_to_bag, adjust_bag, remove_from_bag


class TestBagViews(TestCase):
    """
    Test that the shopping bag works as expected
    """

    fixtures = [
        'categories.json',
        'products.json',
    ]

    def setUp(self):
        self.category = Category.objects.create(
            name='testcategory',
            friendly_name='Test Category'
        )

        self.item = Product.objects.create(
            category=self.category,
            name='test product',
            description='testing product description',
            price=0.01,
        )

        self.quantity = 1

        self.empty_bag = {}

        self.filled_bag = {'14': 1, '11': 1}

        self.bad_bag = {'200': 1}
