from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from products.models import Product, Category
from orders.models import Order

class ViewSetsTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()

        # Criando categoria de teste
        self.category = Category.objects.create(
            name='Eletrônicos', description='Produtos eletrônicos'
        )

        # Criando produto de teste
        self.product = Product.objects.create(
            name='Smartphone', description='Telefone inteligente', 
            price=1500.00, category=self.category
        )

        # Criando pedido de teste
        self.order = Order.objects.create(
            product=self.product, quantity=2, total_price=3000.00
        )

    # Testes Category
    def test_list_categories(self):
        response = self.client.get('/api/categories/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_create_category(self):
        response = self.client.post('/api/categories/', {'name': 'Livros', 'description': 'Todos os livros'})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Category.objects.count(), 2)

    # Testes Product
    def test_list_products(self):
        response = self.client.get('/api/products/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_create_product(self):
        response = self.client.post('/api/products/', {
            'name': 'Notebook', 
            'description': 'Notebook novo',
            'price': 3500.00,
            'category': {'id': self.category.id, 'name': self.category.name, 'description': self.category.description}
        }, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Product.objects.count(), 2)

    # Testes Order
    def test_list_orders(self):
        response = self.client.get('/api/orders/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_create_order(self):
        response = self.client.post('/api/orders/', {
            'product': self.product.id,
            'quantity': 3,
            'total_price': 4500.00
        }, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Order.objects.count(), 2)
