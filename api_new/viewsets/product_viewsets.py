from rest_framework import viewsets
from api_new.models.product import Product
from api_new.serializers.product_serializer import ProductSerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
