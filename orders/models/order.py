from django.db import models
from django.contrib.auth.models import User
from products.models import Product
from django.utils import timezone

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    total_price = models.DecimalField(max_digits=8, decimal_places=2)
    date = models.DateTimeField(default=timezone.now)  # para existing rows

    class Meta:
        ordering = ['id']

    def __str__(self):
        return f'Order {self.id} - {self.user.username}'
