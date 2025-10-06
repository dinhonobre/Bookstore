from rest_framework import viewsets
from api_new.models.order import Order
from api_new.serializers.order_serializer import OrderSerializer

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

