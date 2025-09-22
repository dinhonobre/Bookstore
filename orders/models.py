from django.db import models
from django.contrib.auth.models import User

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # obrigatório para testes
    total_price = models.DecimalField(max_digits=8, decimal_places=2)

    class Meta:
        ordering = ['id']

    def __str__(self):
        return f'Order {self.id} - {self.user.username}'
