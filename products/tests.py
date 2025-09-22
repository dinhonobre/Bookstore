from decimal import Decimal
from django.test import TestCase
from .models import Product, Category
from .serializers import ProductSerializer, CategorySerializer

class ProductSerializerTest(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name="Livros", description="Categoria de livros")
        self.product = Product.objects.create(name="Django Book", description="Aprenda Django", price=50.0, category=self.category)

    def test_product_serializer(self):
        serializer = ProductSerializer(self.product)
        data = serializer.data
        self.assertEqual(data['name'], "Django Book")
        self.assertEqual(data['category']['name'], "Livros")
