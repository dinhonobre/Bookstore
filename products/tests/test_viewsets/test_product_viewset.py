from django.test import TestCase
from rest_framework.test import APIClient
from products.models.product import Product
from products.models.category import Category

class ProductViewSetTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.category = Category.objects.create(name="Livros")
        for i in range(10):
            Product.objects.create(
                name=f"Livro {i}",
                price=i + 10,  # valor do preço
                category=self.category
            )

    def test_product_list_public(self):
        response = self.client.get('/api/products/')
        self.assertEqual(response.status_code, 200)
        self.assertIn('results', response.data)
