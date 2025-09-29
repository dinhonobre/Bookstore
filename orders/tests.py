from decimal import Decimal
from django.test import TestCase
from products.models import Product, Category
from .models import Order
from .serializers import OrderSerializer

class OrderSerializerTest(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name="Livros", description="Categoria de livros")
        self.product = Product.objects.create(name="Django Book", description="Aprenda Django", price=50.0, category=self.category)
        self.order = Order.objects.create(product=self.product, quantity=2, total_price=100.0)

    def test_order_serializer(self):
        serializer = OrderSerializer(self.order)
        data = serializer.data
        self.assertEqual(Decimal(data['total_price']), Decimal('100.00'))
        self.assertEqual(data['product'], self.product.id)
