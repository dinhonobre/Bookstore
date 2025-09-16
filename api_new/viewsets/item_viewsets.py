from rest_framework import viewsets
from api_new.models.item import Item
from api_new.serializers.item_serializer import ItemSerializer

class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
