from decimal import Decimal
from django.test import TestCase
from products.models.product import Product
from products.models.category import Category
from products.serializers.product_serializer import ProductSerializer
from products.serializers.category_serializer import CategorySerializer

class ProductSerializerTest(TestCase):
    def setUp(self):
        self.category = Category.objects.create(
            name="Livros",
            description="Categoria de livros"
        )
        self.product = Product.objects.create(
            name="Django Book",
            description="Aprenda Django",
            price=Decimal('50.00'),  # melhor usar Decimal para precisão
            category=self.category
        )

    def test_product_serializer(self):
        serializer = ProductSerializer(self.product)
        data = serializer.data
        self.assertEqual(data['name'], "Django Book")
        self.assertEqual(data['category']['name'], "Livros")
