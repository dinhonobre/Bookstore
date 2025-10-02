from rest_framework import serializers
from orders.models import Order

class OrderSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()  # mostra o username

    class Meta:
        model = Order
        fields = ['id', 'user', 'total_price']  # somente os campos existentes
