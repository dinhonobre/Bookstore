from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from orders.models.order import Order
from orders.serializers.order_serializer import OrderSerializer
from rest_framework.pagination import PageNumberPagination

class OrderPagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 20

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    pagination_class = OrderPagination
    permission_classes = [IsAuthenticated]  # rota privada
