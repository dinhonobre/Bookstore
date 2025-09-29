from django.test import TestCase
from rest_framework.test import APIClient
from django.contrib.auth.models import User
from .models import Order

class OrderViewSetTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='1234')
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)
        self.order = Order.objects.create(total_price=100.0, user=self.user)

    def test_order_list_authenticated(self):
        response = self.client.get('/api/orders/')
        self.assertEqual(response.status_code, 200)
        self.assertTrue('results' in response.data)

    def test_order_requires_authentication(self):
        self.client.force_authenticate(user=None)
        response = self.client.get('/api/orders/')
        self.assertEqual(response.status_code, 401)
